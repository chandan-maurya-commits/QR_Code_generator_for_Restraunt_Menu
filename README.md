# QR Code Generator for Restaurant Menu

A Django-based web application that allows restaurant owners to generate downloadable QR codes for their digital menus. Users can enter a restaurant name and menu URL, and the application instantly creates a QR code that can be downloaded and shared with customers.

## Features

- Generate QR codes from menu URLs
- Download generated QR codes as PNG images
- Form validation using Django Forms
- Media file handling for QR code storage
- Responsive UI with Bootstrap 5
- Fast and easy QR generation

## Tech Stack

- Python
- Django
- HTML
- Bootstrap 5
- SQLite
- QRCode Library

## Project Structure

```text
QR_Code_generator_for_Restaurant_Menu/
│
├── Templates/
│   ├── generate_qr_code.html
│   └── qr_result.html
│
├── django_qr/
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── settings.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── .gitignore
```

## Installation

### Clone Repository

```bash
git clone https://github.com/chandan-maurya-commits/QR_Code_generator_for_Restraunt_Menu.git
cd QR_Code_generator_for_Restraunt_Menu
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Virtual Environment

Windows:

```bash
env\Scripts\activate
```

Linux/Mac:

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000/
```

## How It Works

1. Enter the restaurant name.
2. Enter the menu URL.
3. Click **Generate QR Code**.
4. The application creates a QR code image.
5. Download and share the QR code with customers.

## Future Improvements

- User Authentication
- QR Code Color Customization
- Logo Embedding in QR Code
- QR Scan Analytics
- QR History Dashboard
- Cloud Storage Integration

## Learning Outcomes

- Django Forms
- URL Routing
- Media File Handling
- QR Code Generation
- Template Rendering
- Bootstrap Integration
- Backend Development with Django

## Author

**Chandan Maurya**

- B.Tech CSE Student
- Backend Developer
- Django Enthusiast
- Aspiring Data Scientist
