# Generated by Django 4.0 on 2022-01-26 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_student_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='comment',
        ),
    ]