from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=70)
    student_email = models.EmailField(max_length=70)
    student_password = models.CharField(max_length=70)


    def __str__(self):
        return self.student_name


class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    re_password = models.CharField(max_length=50)