from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


def above_eighteen(value):
    if value < 18:
        raise ValidationError("Age must be above 18.")
    return value


class ModifiedMixin(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EmployeeProject(models.Model):
    employee_id = models.ForeignKey('Employees', on_delete=models.CASCADE)


class Department(ModifiedMixin, models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, null=True, unique=True)

    def __str__(self):
        return f"{self.pk} {self.name}"


class Project(models.Model):
    name = models.CharField(max_length=100)
    size = models.PositiveIntegerField()


class Employees(models.Model):
    LEVEL_JUNIOR = 'jun'
    LEVEL_MIDDLE = 'mid'
    LEVEL_SENIOR = 'sin'
    LEVEL_CHOICES = (
        (LEVEL_JUNIOR, 'Junior'),
        (LEVEL_MIDDLE, 'Middle'),
        (LEVEL_SENIOR, 'Senior'),
    )

    department = models.ForeignKey(to=Department, on_delete=models.RESTRICT, null=True)

    first_name = models.CharField(max_length=30, verbose_name="First name")
    last_name = models.CharField(max_length=40)

    description = models.TextField(default="Should be filled in.")

    age = models.IntegerField(validators=[above_eighteen])
    experience = models.PositiveIntegerField()
    birth_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    is_manager = models.BooleanField(default=None)

    email = models.EmailField(unique=True)

    level = models.CharField(max_length=len(LEVEL_SENIOR), choices=LEVEL_CHOICES, default=LEVEL_JUNIOR)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"ID: {self.pk}; Names: {self.full_name}"

    def get_absolute_url(self):
        return reverse('employee_details', kwargs={'pk': self.pk})


class Profile(models.Model):
    DESK_ONE = 'first'
    DESK_TWO = 'last'
    DESK_CHOICES = (
        (DESK_ONE, 'desk 1'),
        (DESK_TWO, 'desk 2'),
    )
    desk = models.CharField(choices=DESK_CHOICES)
    employee = models.OneToOneField(Employees, on_delete=models.CASCADE, primary_key=True)


class NullBlankDemo(models.Model):
    custom_id = models.BigAutoField(primary_key=True)

    blank = models.IntegerField(blank=True, null=False)

    null = models.IntegerField(blank=False, null=True)

    blank_null = models.IntegerField(blank=True, null=True)

    default = models.IntegerField(blank=False, null=False)


class Salary(models.Model):

    class Meta:
        verbose_name_plural = "Salaries"

    amount = models.PositiveIntegerField()

    def get_without_taxes_amount(self):
        return self.amount - (self.amount * 0.2)

    @property
    def with_currency(self):
        return f"{self.amount} USD"
