# 🎬 IMDB Clone API

A RESTful API built with Django and Django REST Framework that replicates core features of IMDb, including movie listings, user reviews, JWT authentication, and more.

## 🚀 Features

- JWT Authentication (Login/Register)
- Add, Update, Delete Reviews
- Watchlist CRUD
- Rating system with average update
- Prevent duplicate reviews
- Filtering, Searching & Ordering
- Custom Permissions & Throttling

## 🛠️ Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SimpleJWT
- SQLite 
- Postman for API testing

## 🔧 Setup Instructions

```bash
git clone https://github.com/mehedisam/IMDB_Clone.git
cd IMDB_Clone
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
