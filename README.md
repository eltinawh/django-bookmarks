# django-bookmarks
A Django app

## Key Features
1. User authentication
   - User registration, login, logout, password change, and password reset
   - User profile with profile picture
   - Social authentication using Google OAuth2

2. Image bookmarking from external site

3. Tracking user actions
   - Follow system: A user can follow other users.
   - Activity streams: new user created account, a user bookmarked an image, a user likes an image, a user is following another user
   - Image views counting and ranking

## Requirement

Before you begin, make sure you have the following installed:
- Python 3.11 or higher
- pip (Python package installer)
- venv (Python virtual environment manager)
- git (version control system)
- docker (containerization platform)

We will use Django version >=5.1.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/eltinawh/django-bookmarks.git

# navigate to the project directory
cd django-bookmarks
```

### 2. Set up a virtual environment
```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment (Linux/MacOS)
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations

Run the following commands to create the necessary database tables 
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

To access the Django admin panel, create a superuser account:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up the admin credentials.

### 6. Install Redis docker image

Features like image views counting and ranking utilize Redis, a fast in-memory storage, to enhance performance by avoiding excessive querying to database. We will use the Redis docker image.
```bash
docker pull redis:7.4.2
docker run -it --rm --name redis -p 6379:6379 redis:7.4.2
# Server initialized
# * Ready to accept connections
```
Keep the Redis server running.


### 7. Run the development server

Start the development server to verify everything is working correctly.
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser to see the application.

To be able to try image bookmarking functionality, the development server has to be run in secure mode with this command.
```bash
python manage.py runserver_plus --cert-file cert.crt
```
Then navigate to `https://127.0.0.1:8000/` in your browser.

## Technical Details

### Project Structure
This project consists of the following apps:

1. **Account App**

2. **Images App**

3. **Actions App**


## Documentation

[Official Django Documentation](https://www.djangoproject.com/)
