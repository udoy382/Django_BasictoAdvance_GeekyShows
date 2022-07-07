from django.db import models
from .managers import CustomManager

# Create your models here.

# username = admin
# password = admin

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    # objects = models.Manager() # by default set

    # students = models.Manager() # set our own objects manager


    # ----------Custom Manager------------

    students = CustomManager()


class ProxyStudent(Student):
    students = CustomManager()
    class Meta:
        proxy = True
        ordering = ['name']