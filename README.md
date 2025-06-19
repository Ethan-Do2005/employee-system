# Employee Management System (Django) - Minh Tri Do

A Django RESTful API project for managing employees, departments, attendance, and performance, built with PostgreSQL and Docker. Includes JWT authentication, API documentation (Swagger), and basic data visualizations (pie & bar charts).

---

## 🚀 Features

- CRUD API for Employees, Departments, Attendance, Performance
- JWT-based authentication
- API documentation via Swagger UI
- Filtering, sorting, and pagination for large datasets
- Visualizations:  
  - Employees per Department (Pie Chart)
  - Monthly Attendance Overview (Bar Chart)
- Fully containerized (Docker & Docker Compose)
- Easy seed script for demo data

---

## 🏗️ Project Structure
Employee-System/
│
├── employee_project/
│ └── settings.py, urls.py, ...
│
├── employees/
│ ├── models.py, serializers.py, views.py, ...
│ └── management/commands/seed_data.py
│
├── templates/
│ └── pie_chart.html, bar_chart.html
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env.example


---

## ⚙️ Setup & Usage

## 1. Clone the repository
```bash
git clone https://github.com/Ethan-Do2005/employee-system.git
```

## 2. Build and run with Docker
docker-compose up --build

## 3. Apply migrations & create superuser
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

## 4. Seed demo data
docker-compose exec web python manage.py seed_data

## Django Run
Django runs: http://localhost:8000

## 📄 API Documentation
Swagger UI: http://localhost:8000/swagger/

## Access the admin site
Admin: http://localhost:8000/admin/

## 📊 Visualization Pages
Employees per Department Pie Chart: http://localhost:8000/pie-chart/
Monthly Attendance Overview Bar Chart: http://localhost:8000/bar-chart/

## 📝 .env.example
DEBUG=True
SECRET_KEY=your_secret_key_here
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432

🧹 Notes
1. Make sure Docker Desktop is running before docker-compose up.
2. All development data is stored in Docker volumes (postgres_data).
3. To reset everything (including database): docker-compose down -v


