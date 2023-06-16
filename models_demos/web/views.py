from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Employees, Department, Salary


def index(request):

    employees = Employees.objects.all()
    employees2 = Employees.objects.filter(level='sin')

    department = Department.objects.get(pk=2)
    # department = get_object_or_404(Department, pk=1)
    salary = Salary.objects.get(pk=1)

    context = {
        "employees": employees,
        "employees2": employees2,
        "fun_department": department,
        "salary": salary,
    }

    return render(request, 'web/index.html', context)


def details_employee(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    context = {
        "employee": employee
    }

    return render(request, "web/details.html", context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    employee.delete()
    return redirect('index')


def details_department(request, pk, slug):
    department = get_object_or_404(Department, pk=pk, slug=slug)
    context = {
        "department": department,
    }

    return render(request, "web/details_department.html", context)
