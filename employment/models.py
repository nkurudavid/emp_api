from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=100, blank=False, unique=True)
    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ['department']

    def __str__(self):
        return self.department
    def get_absolute_url(self):
        return reverse('department_info', kwargs={'pk': self.pk})

class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False,)
    last_name = models.CharField(max_length=100, blank=False,)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone_number = PhoneNumberField(blank=False, unique=True)
    dateJoined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to="profile_picture", null=True)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ['first_name']
    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

    def get_absolute_url(self):
        return reverse('employee_info', kwargs={'pk': self.pk})

