# Notice API (Django REST Framework)

## Setup
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Open: http://127.0.0.1:8000/api/notice/

## Endpoints
GET       /api/notice/        list notices
GET       /api/notice/<id>/   get one notice
POST      /api/notice/        create notice
PUT/PATCH /api/notice/<id>/   update notice
DELETE    /api/notice/<id>/   delete notice

## Extra features on GET /api/notice/
?search=exam        search in title and description
?category=holiday   filter by category
?is_active=true     filter active / inactive
?ordering=-created_at   sort (minus = descending)
?page=2             pagination (10 per page)
