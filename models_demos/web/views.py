from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Employees, Department


def index(request):

    employees = Employees.objects.all()
    employees2 = Employees.objects.filter()

    # department = Department.objects.get(pk=4)
    department = get_object_or_404(Department, pk=1)

    context = {
        "employees": employees,
        "employees2": employees2,
        "fun_department": department,
    }

    return render(request, 'web/index.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    employee.delete()
    return redirect('index')
