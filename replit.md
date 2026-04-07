# Bili E-Commerce App

## Overview
A Flask-based e-commerce web application called "Bili" with MongoDB as the database. Features include user authentication, product listings, shopping cart, wishlist, and order management.

## Architecture

- **Framework**: Flask (Python 3.12)
- **Database**: MongoDB (local, port 27017)
- **Authentication**: Flask-Login with MongoDB-backed user storage
- **Forms**: Flask-WTF + WTForms
- **Frontend**: Jinja2 templates + Bootstrap + jQuery

## Project Structure

```
/
├── main.py              # App entry point (runs on 0.0.0.0:5000)
├── app.py               # Alternate entry point
├── start.sh             # Startup script (starts MongoDB then Flask)
├── website/
│   ├── __init__.py      # App factory, MongoDB connection setup
│   ├── models.py        # Data models (Customer, Product, Cart, Order)
│   ├── views.py         # Home/shop routes
│   ├── auth.py          # Auth routes (login, signup, logout)
│   ├── admin.py         # Admin blueprint
│   ├── forms.py         # WTForms form classes
│   ├── template/        # Jinja2 HTML templates
│   └── static/          # CSS, JS, images
```

## Key Dependencies

- flask, flask-login, flask-wtf, werkzeug
- pymongo, bson
- wtforms, email-validator
- gunicorn (for production)

## Running the App

```bash
bash start.sh
```

This starts:
1. MongoDB on `127.0.0.1:27017` with data in `/home/runner/data/db`
2. Flask development server on `0.0.0.0:5000`

## MongoDB Configuration

- Host: `localhost:27017`
- Database: `mydatabase`
- Collections: `customers`, `products`, `carts`, `orders`

## Deployment

- Target: VM (always-running, needed for local MongoDB)
- Run command: `bash start.sh`
