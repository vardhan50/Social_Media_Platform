# Social Media Dashboard

A Django-based web application that allows users to register, log in, and view a simple dashboard displaying their social media handles (Twitter & Facebook).  
This project uses **dummy data** (no real API integration) and is intended for learning or demo purposes.

---

## Features

- User registration and authentication
- Profile creation using Django signals
- Dashboard with user-specific social media handles
- Dummy post/comment data (can be extended)
- Clean Django project structure

---

## Tech Stack

- **Backend:** Django 4.2.18
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Language:** Python 3.9+

---


## ⚙️ Setup Instructions

1. **Clone the repository**
   --> git clone https://github.com/yourusername/social-media-dashboard.git
   --> cd social_media_dashboard

2. **create and activate a virtual environment**
    --> python -m venv env
    # On Windows:
    --> env\Scripts\activate
    # On macOS/Linux:
    --> source env/bin/activate

3. **Install Django**
     --> pip install django

4. **Apply migrations**
    --> python manage.py makemigrations
    --> python manage.py migrate

5. **Run the development server**
    --> python manage.py runserver

   

