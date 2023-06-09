from django.contrib import admin

from models_demos.web.models import Employees, NullBlankDemo, Department, Project, Profile, Salary


@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name', 'age', 'level']
    list_filter = ['level']
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(NullBlankDemo)
class NullBlankDemo(admin.ModelAdmin):
    pass


@admin.register(Department)
class Department(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    pass
