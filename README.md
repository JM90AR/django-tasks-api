# Django Tasks API

A REST API for task management built with Django and Django REST Framework.

## Features

- JWT authentication
- Full CRUD for tasks
- Filter tasks by status (`?completada=true/false`)
- Search tasks by title or description (`?search=texto`)
- Order results (`?ordering=titulo` or `?ordering=-creada`)
- Pagination (10 results per page)
- User registration with automatic token generation

## Tech Stack

- Python
- Django 6
- Django REST Framework
- SimpleJWT
- SQLite (development)

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/JM90AR/django-tasks-api.git
cd django-tasks-api
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the server
```bash
python manage.py runserver
```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/registro/` | Register a new user |
| POST | `/api/token/` | Obtain JWT access and refresh tokens |
| POST | `/api/token/refresh/` | Refresh access token |

### Tasks

All task endpoints require `Authorization: Bearer <access_token>` header.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tareas/` | List all tasks |
| POST | `/api/tareas/` | Create a task |
| GET | `/api/tareas/{id}/` | Retrieve a task |
| PATCH | `/api/tareas/{id}/` | Partially update a task |
| PUT | `/api/tareas/{id}/` | Fully update a task |
| DELETE | `/api/tareas/{id}/` | Delete a task |

## Usage Examples

### Register a user
```bash
curl -X POST http://127.0.0.1:8000/api/registro/ \
  -H "Content-Type: application/json" \
  -d '{"username": "miguel", "password": "mypassword"}'
```

Response:
```json
{
    "token": "your_token_here",
    "username": "miguel"
}
```

### Obtain JWT token
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "miguel", "password": "mypassword"}'
```

Response:
```json
{
    "access": "eyJhbGci...",
    "refresh": "eyJhbGci..."
}
```

### Create a task
```bash
curl -X POST http://127.0.0.1:8000/api/tareas/ \
  -H "Authorization: Bearer " \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Learn Django", "descripcion": "Models, views, and URLs"}'
```

### Filter and search
```bash
# Only incomplete tasks
GET /api/tareas/?completada=false

# Search by text
GET /api/tareas/?search=django

# Order by title
GET /api/tareas/?ordering=titulo

# Combine filters
GET /api/tareas/?completada=false&search=django&ordering=-creada
```

## Project Structure
```
django-api/
    config/
        settings.py
        urls.py
    tareas/
        models.py
        views.py
        serializers.py
        urls.py
    requirements.txt
    manage.py
```

## Author

José Miguel Alba Rodríguez
- GitHub: [@JM90AR](https://github.com/JM90AR)