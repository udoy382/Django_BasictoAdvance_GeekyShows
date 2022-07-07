from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    # ***********import signals from blog for connect and use django signal**********
    def ready(self):
        import blog.signals