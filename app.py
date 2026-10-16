import click
import os
from flask import Flask, render_template, redirect, request, flash
from flask.signals import message_flashed          # FIX: was 'from flask import'
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate                  # NEW
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime, timezone

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-fallback-key")


@message_flashed.connect_via(app)
def log_task_activities(sender, message, category):
    print(f"Log triggered | Sender: {sender} | Category: {category} | Message: {message}")


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)
migrate = Migrate(app, db)                         # NEW — replaces db.create_all()


class Task(db.Model):
    def __repr__(self):
        return f"<Task {self.title}>"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    priority: Mapped[str] = mapped_column(db.String(10), nullable=False, default="medium")  # FIX


# REMOVED db.create_all() — flask-migrate handles this now


# CLI command to add task from terminal
@app.cli.command("add-task")
@click.argument("title")
def add_task(title):
    task = Task(title=title)
    db.session.add(task)
    db.session.commit()
    print(f"Task '{title}' added.")


@app.route("/")
def home():
    filter_param = request.args.get("filter", "all")
    search_query = request.args.get("q", "").strip()

    query = db.select(Task)

    if filter_param == "completed":
        query = query.where(Task.completed)
    elif filter_param == "pending":
        query = query.where(~Task.completed)

    if search_query:
        query = query.where(Task.title.ilike(f"%{search_query}%"))

    all_tasks = db.session.execute(query).scalars().all()

    return render_template(
        "index.html",
        tasks=all_tasks,
        current_filter=filter_param,
        search_query=search_query,
    )


@app.route("/add", methods=["POST"])
def add_tasks():
    title = request.form.get("title")
    if not title or not title.strip():
        return redirect("/")
    task = Task(title=title.strip())
    db.session.add(task)
    db.session.commit()
    flash("Task added successfully!", "success")
    return redirect("/")


@app.route("/complete/<int:task_id>/", methods=["POST"])
def complete_task(task_id):
    task = db.get_or_404(Task, task_id)
    task.completed = not task.completed
    db.session.commit()
    flash("Task updated!", "success")
    return redirect("/")


@app.route("/delete/<int:task_id>/", methods=["POST"])
def remove_task(task_id):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully!", "success")
    return redirect("/")


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = db.get_or_404(Task, task_id)
    if request.method == "POST":
        title = request.form.get("title")
        if title and title.strip():
            task.title = title.strip()
            db.session.commit()
            flash("Task edited successfully!", "success")
        return redirect("/")
    return render_template("edit.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)