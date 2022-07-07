from django.db import models

# Create your models here.

# Username = admin
# Password = admin

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()


class Teacher(models.Model):
    name = models.CharField(max_length=70)
    empname = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    salary =  models.IntegerField()
    join_date = models.DateField()