from django.core.management.base import BaseCommand
from employees.models import Department, Employee, Attendance, Performance
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with fake employees, departments, attendance, and performance data'

    def handle(self, *args, **kwargs):
        # Create Departments
        department_names = ['Engineering', 'HR', 'Sales', 'Marketing', 'Finance']
        departments = []

        for name in department_names:
            dept, created = Department.objects.get_or_create(department_name=name)
            departments.append(dept)

        self.stdout.write(self.style.SUCCESS(f"✅ Created {len(departments)} departments"))

        # Create Employees
        for _ in range(50):
            emp = Employee.objects.create(
                employee_name=fake.name(),
                employee_mail=fake.unique.email(),
                employee_phone=fake.msisdn()[0:10],
                employee_address=fake.address(),
                employee_date_of_joining=fake.date_between(start_date='-2y', end_date='today'),
                employee_department=random.choice(departments),
            )

            # Create Attendance Records
            for _ in range(5):
                Attendance.objects.create(
                    attendance_employee=emp,
                    attendance_date=fake.date_between(start_date='-30d', end_date='today'),
                    attendance_status=random.choice(['Present', 'Absent', 'Late']),
                )

            # Create Performance Reviews
            for _ in range(2):
                Performance.objects.create(
                    performance_employee=emp,
                    performance_rating=random.randint(1, 5),
                    performance_review_date=fake.date_between(start_date='-1y', end_date='today'),
                )

        self.stdout.write(self.style.SUCCESS("🎉 Successfully seeded 50 employees with attendance and performance data"))
