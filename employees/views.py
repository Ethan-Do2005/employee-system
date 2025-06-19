from django.shortcuts import render
from rest_framework import viewsets
from .models import Department, Employee, Attendance, Performance
from .serializers import *
from django.db.models import Count
import json
from django.db.models.functions import TruncMonth

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ['employee_department', 'employee_name', 'employee_date_of_joining']
    ordering_fields = ['employee_name', 'employee_date_of_joining', 'id']
    ordering = ['id']

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

def employee_pie_chart(request):
    data = (
        Employee.objects.values('employee_department__department_name')
        .annotate(count=Count('id'))
        .order_by('employee_department__department_name')
    )
    labels = [d['employee_department__department_name'] for d in data]
    values = [d['count'] for d in data]
    return render(request, 'charts.html', {
        'labels': json.dumps(labels),
        'values': json.dumps(values),
    })

def attendance_bar_chart(request):
    data = (
        Attendance.objects
        .annotate(month=TruncMonth('attendance_date'))
        .values('month', 'attendance_status')
        .annotate(count=Count('id'))
        .order_by('month')
    )

    months = sorted(list(set([d['month'].strftime("%Y-%m") for d in data])))
    statuses = sorted(list(set([d['attendance_status'] for d in data])))

    chart_data = {status: [0]*len(months) for status in statuses}
    for d in data:
        month_idx = months.index(d['month'].strftime("%Y-%m"))
        chart_data[d['attendance_status']][month_idx] = d['count']

    return render(request, 'attendance_chart.html', {
        'months': json.dumps(months),
        'statuses': json.dumps(statuses),
        'chart_data': json.dumps([{'label': s, 'data': chart_data[s]} for s in statuses]),
    })
