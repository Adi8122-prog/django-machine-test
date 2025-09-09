# Django Machine Test - Client Project Management API

This is a Django REST Framework API for managing clients, projects, and user assignments. The API provides endpoints for creating clients, managing projects, and assigning users to projects.

## Features

- **Client Management**: Create, read, update, and delete clients
- **Project Management**: Create projects under clients and assign users
- **User Assignment**: Assign multiple users to projects
- **Authentication**: JWT token-based authentication
- **Admin Interface**: Django admin for user management

## API Endpoints

### Authentication
- `POST /api/token/` - Get access token (login)
- `POST /api/token/refresh/` - Refresh access token

### Clients
- `GET /api/clients/` - List all clients
- `POST /api/clients/` - Create a new client
- `GET /api/clients/:id/` - Get client details with projects
- `PUT/PATCH /api/clients/:id/` - Update client
- `DELETE /api/clients/:id/` - Delete client

### Projects
- `POST /api/clients/:id/projects/` - Create project for a client
- `GET /api/projects/` - Get projects assigned to logged-in user

### Users (Optional - for testing)
- `GET /api/users/` - List all users
- `POST /api/users/register/` - Register a new user

## Database Setup

### Option 1: PostgreSQL (Recommended)

1. **Install PostgreSQL**
   ```bash
   # Download and install PostgreSQL from https://www.postgresql.org/download/
   ```

2. **Create Database**
   ```sql
   -- Connect to PostgreSQL as superuser
   CREATE DATABASE machine_test_db;
   CREATE USER postgres WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE machine_test_db TO postgres;
   ```

3. **Update Environment Variables**
   ```env
   DB_NAME=machine_test_db
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

### Option 2: MySQL

1. **Install MySQL**
   ```bash
   # Download and install MySQL from https://dev.mysql.com/downloads/mysql/
   ```

2. **Create Database**
   ```sql
   -- Connect to MySQL as root
   CREATE DATABASE machine_test_db;
   CREATE USER 'root'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON machine_test_db.* TO 'root'@'localhost';
   FLUSH PRIVILEGES;
   ```

3. **Update settings.py**
   - Comment out PostgreSQL configuration
   - Uncomment MySQL configuration in `machine_test/settings.py`

4. **Update Environment Variables**
   ```env
   DB_NAME=machine_test_db
   DB_USER=root
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=3306
   ```

## Installation & Setup

### 1. Clone the Repository
```bash
# If using git, or just extract the files
cd django_machine_test
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
```bash
# Copy environment template
copy .env.example .env

# Edit .env file with your database credentials
# Update SECRET_KEY, DB_PASSWORD, etc.
```

### 5. Database Migrations
```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
# Create admin user for Django admin
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
# Start the development server
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## How to Test the API

### 1. Get Authentication Token
```bash
POST http://127.0.0.1:8000/api/token/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

### 2. Create a Client
```bash
POST http://127.0.0.1:8000/api/clients/
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
    "client_name": "Nimap"
}
```

### 3. List All Clients
```bash
GET http://127.0.0.1:8000/api/clients/
Authorization: Bearer <your_access_token>
```

### 4. Get Client Details
```bash
GET http://127.0.0.1:8000/api/clients/1/
Authorization: Bearer <your_access_token>
```

### 5. Update Client
```bash
PUT http://127.0.0.1:8000/api/clients/1/
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
    "client_name": "Updated Company Name"
}
```

### 6. Create Project for Client
```bash
POST http://127.0.0.1:8000/api/clients/1/projects/
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
    "project_name": "Project A",
    "users": [
        {
            "id": 1,
            "name": "Rohit"
        }
    ]
}
```

### 7. List User's Projects
```bash
GET http://127.0.0.1:8000/api/projects/
Authorization: Bearer <your_access_token>
```

### 8. Delete Client
```bash
DELETE http://127.0.0.1:8000/api/clients/1/
Authorization: Bearer <your_access_token>
```

## Project Structure

```
django_machine_test/
├── manage.py
├── requirements.txt
├── .env.example
├── README.md
├── machine_test/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── api/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── urls.py
    └── views.py
```

## Models

### User (Django's built-in User model)
- id, username, email, first_name, last_name

### Client
- id, client_name, created_at, created_by, updated_at

### Project
- id, project_name, client (FK), users (M2M), created_at, created_by

## Database Design

The system uses the following relationships:
- One User can create many Clients (1:M)
- One User can create many Projects (1:M)
- One Client can have many Projects (1:M)
- One Project can be assigned to many Users (M:M)
- Many Users can be assigned to many Projects (M:M)

## API Response Examples

### List Clients
```json
[
    {
        "id": 1,
        "client_name": "Nimap",
        "created_at": "2019-12-24T11:03:55.931739+05:30",
        "created_by": "Rohit"
    }
]
```

### Client Detail with Projects
```json
{
    "id": 2,
    "client_name": "Infotech",
    "projects": [
        {
            "id": 1,
            "name": "project A"
        }
    ],
    "created_at": "2019-12-24T11:03:55.931739+05:30",
    "created_by": "Rohit",
    "updated_at": "2019-12-24T11:03:55.931739+05:30"
}
```

### Create Project Response
```json
{
    "id": 3,
    "project_name": "Project A",
    "client": "Nimap",
    "users": [
        {
            "id": 1,
            "name": "Rohit"
        }
    ],
    "created_at": "2019-12-24T11:03:55.931739+05:30",
    "created_by": "Ganesh"
}
```

## Admin Panel

Access the Django admin at `http://127.0.0.1:8000/admin/`
- Create and manage users
- View clients and projects
- Assign users to projects

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Check your database credentials in `.env`
   - Ensure database server is running
   - Verify database and user exist

2. **Migration Errors**
   ```bash
   # Reset migrations if needed
   python manage.py migrate --run-syncdb
   ```

3. **Import Errors**
   - Ensure virtual environment is activated
   - Install all requirements: `pip install -r requirements.txt`

4. **Authentication Issues**
   - Ensure you're sending the JWT token in the Authorization header
   - Token format: `Authorization: Bearer <token>`

## Development Notes

- The API uses JWT tokens for authentication
- All endpoints except authentication require authentication
- Users can only see projects they're assigned to
- Clients can only be created by authenticated users
- The system uses timezone-aware datetime fields

## Production Deployment

For production deployment:
1. Set `DEBUG=False` in settings
2. Configure a production database
3. Set up proper static file serving
4. Use a production WSGI server like Gunicorn
5. Set up proper logging
6. Configure CORS for frontend integration
