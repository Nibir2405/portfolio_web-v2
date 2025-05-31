# Portfolio Web

A personal portfolio website built with Django, showcasing projects, skills, and a contact form. This project is designed to highlight your experience, technical skills, and completed works, with a modern responsive UI.

## Features

- **Home Page:** Introduction and quick links.
- **About Section:** Brief bio and background.
- **Skills Section:** Visual representation of technical skills.
- **Projects Section:** List of completed projects with GitHub links.
- **Contact Form:** Visitors can send messages directly from the site.
- **Admin Panel:** Manage contact submissions and site content.
- **Static Assets:** Custom CSS, images, and downloadable resume.

## Project Structure

```
mysite/
    settings.py
    urls.py
    wsgi.py
portfolio_web/
    admin.py
    apps.py
    forms.py
    models.py
    tests.py
    urls.py
    views.py
    migrations/
    templates/
static/
    css/
    images/
    pdf/
manage.py
db.sqlite3
```

## Setup Instructions

1. **Clone the repository**
    ```sh
    git clone <repository-url>
    cd <project-directory>
    ```

2. **Install dependencies**
    ```sh
    pip install django
    ```

3. **Apply migrations**
    ```sh
    python manage.py migrate
    ```

4. **Create a superuser (for admin access)**
    ```sh
    python manage.py createsuperuser
    ```

5. **Run the development server**
    ```sh
    python manage.py runserver
    ```

6. **Access the site**
    - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
    - Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Live Demo

You can view the live version of this portfolio at:  
[https://navid250.pythonanywhere.com](https://navid250.pythonanywhere.com)

## Customization

- **Resume:** Replace `static/pdf/resume.pdf` with your own resume.
- **Images:** Update images in `static/images/` as needed.
- **Projects:** Edit the projects section in [`portfolio_web/templates/home.html`](portfolio_web/templates/home.html).
- **Contact Form:** The form is defined in [`portfolio_web/forms.py`](portfolio_web/forms.py) and submissions are stored in the database via the `Contact` model.

## Technologies Used

- Django 5.x
- HTML5, CSS3
- SQLite (default, can be changed in [`mysite/settings.py`](mysite/settings.py))

## License

This project is for personal and educational use. You may modify and use it as a template for your own portfolio.




**Author:** Navid Ul Islam---
---

**Author:** Navid Ul Islam