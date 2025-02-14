# Django Student and Course Management System

This is a Django project for managing students and courses. The project includes functionality for creating, reading, updating, and deleting student and course records. Additionally, the project has authentication features, allowing users to log in and manage data through the Django admin interface.

## Features

- Class-based views for CRUD operations on students and courses
- Authentication with login, logout, and password management
- Template inheritance with a base template
- Stylish dropdown menu for navigation

## Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Create a Virtual Environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run Migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the Application:**

    Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Project Structure

```plaintext
myproject/
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    studentapp/
        __init__.py
        admin.py
        apps.py
        forms.py
        models.py
        templates/
            registration/
                login.html
            studentapp/
                base.html
                student_list.html
                student_form.html
                course_list.html
                course_form.html
        urls.py
        views.py
    manage.py
