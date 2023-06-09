from django.shortcuts import render
from .models import Employees


def index(request):

    employees = Employees.objects.all()
    employees2 = Employees.objects.all()

    context = {
        "employees": employees,
        "employees2": employees2,
    }

    return render(request, 'web/index.html', context)
