from django.db import models

# Create your models here.

# Username = admin
# Password = admin

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    publish_date = models.DateTimeField()

