from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name
class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_mail = models.EmailField(unique=True)
    employee_phone = models.CharField(max_length=10)
    employee_address = models.CharField(max_length=100)
    employee_date_of_joining =  models.DateField()
    employee_department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name
    
class Attendance(models.Model):
    STATUS_CHOICE = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'), 
    ]
    attendance_employee = models.ForeignKey(Employee, on_delete= models.CASCADE)
    attendance_date = models.DateField()
    attendance_status = models.CharField(max_length=10, choices=STATUS_CHOICE)

    def __str__(self):
        return f"{self.attendance_employee.employee_name} - {self.attendance_date} - {self.attendance_date}"

class Performance(models.Model):
    performance_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    performance_rating = models.IntegerField()
    performance_review_date = models.DateField()

    def __str__(self):
        return f"{self.performance_employee.employee_name} - {self.performance_rating}/5"  
