from django.db import models

# Create your models here.
# ---------------------------------------------------

# Admin Panel Info ~
# Username = Udoy
# Password = admin

# ---------------------------------------------------
class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
