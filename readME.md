# Django CV Project

This project converts my resume (CV) into an HTML page rendered by Django.

---

## Table of Contents

1. [Overview](#overview)  
2. [Requirements](#requirements)  
3. [Installation & Setup](#installation--setup)  
4. [Running the Application](#running-the-application)  
5. [Project Structure](#project-structure)

---

## Overview

- **Purpose:** Convert my CV into a Django-based web application.
- **Technologies:** Python 3, Django, HTML, CSS.
- **Description:** This project uses Django templates to display resume details (education, skills, experience, projects, etc.) in a browser.

---

## Requirements

- **Python:** Version 3.x  
  (Ensure you have Python 3 installed; you can download it from [python.org](https://www.python.org/downloads/))
- **Django:** Version 3.x or 4.x  
  (Install using: `pip install django`)

---

## Installation & Setup

1. **Clone or Download the Repository**

   ```bash
   git clone <your-github-repo-url>
   cd <repository-directory>

## Create and Activate a Virtual Environment

1. **Create the virtual environment:**

   ```bash
   python -m venv venv

2. **Activate the virtual environment:**
   ```bash
   .\venv\Scripts\activate #for windows
   source venv/bin/activate #for mac
   
3. **Install Dependencies**
   ```bash
   pip install django 

## Running the Application

1. **Start the Django Development Server**
   ```bash
   python manage.py runserver

2. **Open in Browser**
    
Open http://127.0.0.1:8000/ in your browser to view the CV page.

5. **Project Structure**
```
cv_django_project/
├── manage.py
├── my_cv/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── cv/
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── cv/
│           └── cv.html
└── README.md
```