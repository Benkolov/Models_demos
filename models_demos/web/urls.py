from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>', views.delete_employee, name='delete_employee'),
    path('epl-details/<int:pk>', views.details_employee, name='employee_details'),
    path('dep-details/<int:pk>/<slug:slug>', views.details_department, name='department_details'),
]
