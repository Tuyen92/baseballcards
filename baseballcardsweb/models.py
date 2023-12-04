from django.db import models
from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import AbstractUser

# Create your models here.


# Create your models here.
class Employees(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=255)
    image = models.CharField(max_length=255, null=True)
    birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True)
    bio = models.CharField(max_length=255)
    level = models.ForeignKey('Levels', on_delete=models.CASCADE)
    speciality = models.ForeignKey('Specialities', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.full_name}'


class Softskills(models.Model):
    soft_skill = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.soft_skill
    

class EmployeeSoftskills(models.Model):
    employee = models.ForeignKey('Employees', on_delete=models.CASCADE)
    soft_skill = models.ForeignKey('Softskills', on_delete=models.CASCADE)
    rate = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.employee.full_name} - {self.soft_skill.soft_skill} - {self.rate}'


class Hardskills(models.Model):
    hard_skill = models.CharField(max_length=255, null=False)\

    def __str__(self):
        return self.hard_skill
    

class EmployeeHardskills(models.Model):
    employee = models.ForeignKey('Employees', on_delete=models.CASCADE)
    hard_skill = models.ForeignKey('Hardskills', on_delete=models.CASCADE)
    rate = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.employee.full_name} - {self.hard_skill.hard_skill} - {self.rate}'


class Languages(models.Model):
    language = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.language
    

class EmployeeLanguages(models.Model):
    employee = models.ForeignKey('Employees', on_delete=models.CASCADE)
    language = models.ForeignKey('Languages', on_delete=models.CASCADE)
    rate = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.employee.full_name} - {self.language} - {self.rate}'
    

class Levels(models.Model):
    level = models.CharField(max_length=255, null=False)
    color = ColorField(default='#000000')

    def __str__(self):
        return self.level
    

class Specialities(models.Model):
    speciality = models.CharField(max_length=255, null=False)
    color = ColorField(default='#000000')

    def __str__(self):
        return self.speciality


class Reference(models.Model):
    employee = models.ForeignKey('Employees', on_delete=models.CASCADE)
    cv = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)

    def __str__(self):
        return self.employee.full_name