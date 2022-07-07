from django.contrib import admin
from .models import Page, Post, Song, My_page, My_post, My_song

# Register your models here.

admin.site.register(Page)
admin.site.register(Post)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_duration', 'written_by']


# -------------Model Relationship Example-------------

@admin.register(My_page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'page_cat', 'page_publish_date', 'user']


@admin.register(My_post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_cat', 'post_publish_date']


@admin.register(My_song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_duration', 'written_by']
