from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# username = admin
# password = admn

class Page(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff':True})
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()


    # --------Many to One Relationship----------

class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #  Delete only User not Post
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_publish_date = models.DateField()

    # ------------Many to Many Relationship------------

class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=70)
    song_duration = models.IntegerField()

    def written_by(self):
        return ', '.join([str(p) for p in self.user.all()])

    
    # -------------Model Relationship Example-------------

class My_page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()

class My_post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_publish_date = models.DateField()

class My_song(models.Model):
    user = models.ManyToManyField(User)

    song_name = models.CharField(max_length=70)
    song_duration = models.IntegerField()

    def written_by(self):
        return ', '.join([str(p) for p in self.user.all()])

