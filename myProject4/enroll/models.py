from django.db import models

# Create your models here.

# username = Udoy
# password = udoy2299

class User(models.Model):
    student_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)