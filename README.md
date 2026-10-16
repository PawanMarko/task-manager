# ✅ Task Manager — Python & Flask

A simple task management web application built with **Python, Flask, Flask-SQLAlchemy, and SQLite**. It allows users to create, edit, delete, search, filter, and mark tasks as completed through a clean, dark-themed web interface.

## 📌 About the Project

This project was created to practice Python backend development, web application routing, database operations, and HTML template rendering using Flask.

The application stores tasks in a local SQLite database and displays them through a custom-designed interface.

## ✨ Features

- ➕ **Add Tasks** — Create new tasks with a title.
- ✏️ **Edit Tasks** — Update an existing task's title.
- ✅ **Mark as Completed** — Toggle a task between completed and pending.
- 🗑️ **Delete Tasks** — Remove tasks from the database.
- 🔍 **Search Tasks** — Find tasks by title.
- 📋 **Filter Tasks** — Display all tasks, completed tasks, or pending tasks.
- 📊 **Task Statistics** — View total, completed, and pending task counts.
- 💾 **Persistent Storage** — Store task data in an SQLite database.
- 🖥️ **Custom UI** — Dark theme with lime accents, styled forms, and interactive task elements.
- 🛠️ **Command-Line Task Creation** — Add a task through a custom Flask CLI command.

## 🛠️ Technologies Used

| Technology       | Purpose                        |
| ---------------- | ------------------------------ |
| Python           | Application logic              |
| Flask            | Web framework and routing      |
| Flask-SQLAlchemy | Database integration and ORM   |
| SQLite           | Local database storage         |
| Flask-Migrate    | Database migration management  |
| HTML5            | Page structure                 |
| CSS3             | Styling and responsive layout  |
| Jinja2           | Dynamic HTML templates         |
| Click            | Flask command-line integration |

## 📂 Project Structure

```text
task-manager/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── edit.html
├── migrations/          # Generated during migration setup
├── instance/
│   └── database.db      # May be created when the app runs
└── README.md
```

**Note:** The `migrations/` and `instance/` directories may be generated locally. Include the migration files in GitHub if you use Flask-Migrate to manage your database schema.

## ⚙️ Installation and Setup

### 1. Install Python

Install Python 3 from [python.org](https://www.python.org/downloads/).

Verify your installation:

```bash
python --version
```

### 2. Clone the Repository

Replace `your-username` with your GitHub username.

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file contains the application's Python dependencies.

### 5. Initialize the Database

This application uses Flask-Migrate. If migration files have not already been created, initialize them:

```bash
flask --app app db init
flask --app app db migrate -m "Create task table"
flask --app app db upgrade
```

Run `db init` only once when creating the migration repository. If the project already contains a valid `migrations/` directory, use the existing migrations and run:

```bash
flask --app app db upgrade
```

### 6. Start the Application

```bash
python app.py
```

Open the local address shown in your terminal, usually:

```text
http://127.0.0.1:5000
```

## 🧭 How to Use

1. Open the application in your browser.
2. Enter a task title and click **Add Task**.
3. Use the checkbox-style control to mark a task completed or pending.
4. Click the edit icon to update a task title.
5. Click the delete icon to remove a task.
6. Use the search field to find tasks by title.
7. Use the filter options, if available in the interface, to view completed or pending tasks.

## 🗄️ Database Model

Each task is represented by a database record with these fields:

| Field        | Description                           |
| ------------ | ------------------------------------- |
| `id`         | Unique task identifier                |
| `title`      | Task title                            |
| `completed`  | Completion status                     |
| `created_at` | Task creation timestamp               |
| `priority`   | Task priority, defaulting to `medium` |

The application uses SQLAlchemy models to interact with the database.

## 💻 Command-Line Usage

The application includes a custom Flask CLI command for adding tasks directly from the terminal:

```bash
flask --app app add-task "Learn Python"
```

The task is saved to the database.

## 🔐 Configuration

The Flask secret key can be configured using the `SECRET_KEY` environment variable.

For local development, the application has a fallback key. **Before deploying the application publicly, set a strong secret key through an environment variable and do not commit secrets to GitHub.**

## ⚠️ Current Limitations

- The application is designed for local use and does not include user accounts or authentication.
- Tasks are stored in a local SQLite database.
- The current edit form updates task titles; it does not provide a priority-editing interface.
- The application runs with Flask's development server and debug mode, which should not be used in production.

## 🚀 Future Improvements

- Add priority selection and priority-based filtering.
- Add due dates and reminders.
- Add user registration and login.
- Add task categories and tags.
- Improve form validation and error handling.
- Add pagination for large task lists.
- Deploy the application using a production-ready WSGI server.

## 🎯 Learning Outcomes

Through this project, I practiced:

- Building routes with Flask.
- Handling GET and POST requests.
- Creating and managing SQLAlchemy database models.
- Performing database CRUD operations.
- Rendering dynamic HTML using Jinja2.
- Searching and filtering database records.
- Managing schema changes with Flask-Migrate.
- Connecting frontend templates to backend functionality.

## 👤 Author

**Your Name**

GitHub: https://github.com/your-username

---

⭐ This project is part of my Python development and backend programming learning journey.
