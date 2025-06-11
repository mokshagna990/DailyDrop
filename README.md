# DailyDrop - A Secure Personal Diary Web Application

## Project Overview

DailyDrop is a lightweight and secure web application designed to help users maintain a personal digital diary. Built with Flask, it provides a simple yet robust platform for users to create, view, edit, and delete their daily entries with secure user authentication. The application focuses on data privacy and a straightforward user experience, allowing individuals to privately record their thoughts and experiences.

## Features

* **User Authentication:** Secure registration and login functionalities using Flask-Login and Bcrypt for password hashing.
* **Personalized Dashboard:** A private dashboard displaying all diary entries for the logged-in user, ordered by most recent.
* **CRUD Operations for Entries:**
    * **Create:** Users can add new diary entries with a title and rich content.
    * **Read:** View existing entries on the dashboard.
    * **Update:** Edit existing entries to modify title or content.
    * **Delete:** Remove unwanted entries with a confirmation prompt.
* **Responsive Design:** Utilizes Bootstrap 5 for a clean, modern, and responsive user interface across various devices.
* **Flashed Messages:** Provides immediate feedback to the user for actions like successful registration, login, or entry updates.
* **Database Integration:** Uses SQLite for data storage, managed with Flask-SQLAlchemy for ORM capabilities and Flask-Migrate for database schema evolution.
* **Modular CSS:** Styles are organized into separate CSS files for better maintainability and reusability.

## Technical Stack

* **Backend Framework:** Flask
* **Database:** SQLite
* **ORM:** Flask-SQLAlchemy
* **User Authentication & Session Management:** Flask-Login
* **Password Hashing:** Flask-Bcrypt
* **Database Migrations:** Flask-Migrate
* **Web Forms:** Flask-WTF
* **Frontend:** HTML, CSS (Custom & Bootstrap 5), Jinja2 Templating

## Project Structure
DailyDrop/
├── app/
│   ├── init.py         # Application factory, initializes extensions
│   ├── models.py           # Defines SQLAlchemy models (User, DiaryEntry)
│   ├── forms.py            # Defines Flask-WTF forms (Register, Login, DiaryEntry)
│   ├── routes.py           # Defines all application routes and logic
│   ├── static/             # Static assets (CSS, JS, images)
│   │   └── css/            # Stylesheets
│   │       ├── base.css
│   │       ├── dashboard.css
│   │       ├── diary_form.css
│   │       ├── login.css
│   │       └── register.css
│   └── templates/          # Jinja2 HTML templates
│       ├── base.html
│       ├── dashboard.html
│       ├── diary_form.html
│       ├── login.html
│       └── register.html
├── instance/
│   └── personal_diary.db   # SQLite database file (will be created automatically)
├── .gitignore              # Specifies intentionally untracked files to ignore
├── requirements.txt        # Lists Python dependencies
└── run.py                  # Entry point to run the Flask application

## Setup and Installation

Follow these steps to get DailyDrop running locally:

### Prerequisites

* Python 3.7+
* pip (Python package installer)

### Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/DailyDrop.git](https://github.com/YOUR_GITHUB_USERNAME/DailyDrop.git)
    cd DailyDrop
    ```
    (Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username)

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set environment variables:**
    Flask applications, especially in production, should use environment variables for sensitive data like `SECRET_KEY`.
    * **On Windows (Command Prompt):**
        ```bash
        set FLASK_APP=run.py
        set SECRET_KEY=your_super_secret_key_here # Replace with a strong, random key
        ```
    * **On Windows (PowerShell):**
        ```bash
        $env:FLASK_APP="run.py"
        $env:SECRET_KEY="your_super_secret_key_here" # Replace with a strong, random key
        ```
    * **On macOS/Linux:**
        ```bash
        export FLASK_APP=run.py
        export SECRET_KEY='your_super_secret_key_here' # Replace with a strong, random key
        ```
    **Note:** For local development, `SECRET_KEY` is hardcoded as `'this_should_be_changed'` in `app/__init__.py`. **For production or sharing, always use an environment variable.**

6.  **Initialize the database:**
    The `db.create_all()` call in `app/__init__.py` will create the SQLite database file and tables upon the first run if they don't exist. You don't need to manually run migrations for initial setup if you're just starting.

7.  **Run the application:**
    ```bash
    flask run
    ```

8.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000/`

## Usage

1.  **Register:** Create a new account with a unique username, email, and password.
2.  **Login:** Use your registered credentials to access your personal dashboard.
3.  **New Entry:** Click "+ New Entry" to write and save your thoughts.
4.  **Manage Entries:** Edit or delete your existing entries from the dashboard.
5.  **Logout:** Securely end your session.

## Contributing

Contributions are welcome! If you have suggestions for improvements, find a bug, or want to add a new feature, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE). (You should create a `LICENSE` file in your repository if you want to explicitly state the license).

## Contact

Mokshagna Doddapaneni - mokshagna990@gmail.com
