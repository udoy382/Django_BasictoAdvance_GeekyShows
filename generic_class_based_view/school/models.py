from django.db import models

# Create your models here.


# Username = admin
# Password = admin

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    course = models.CharField(max_length=70)