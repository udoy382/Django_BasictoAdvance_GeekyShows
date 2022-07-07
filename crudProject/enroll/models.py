from django.db import models

# Create your models here.


# --------------------------------------------

# Admin Panel Info:
# Username = udoy
# Email = srudoy436@gmail.com
# Password = udoy2299

# --------------------------------------------


class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.name