from django.db import models

# Create your models here.
# ---------------------------------------------------

# Admin Panel Info ~
# Username = Udoy
# Email = srudoy436@gmail.com
# Password = srudoy2299 


# ---------------------------------------------------
class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
