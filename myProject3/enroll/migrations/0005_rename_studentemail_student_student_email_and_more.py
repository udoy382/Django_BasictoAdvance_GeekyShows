# Generated by Django 4.0 on 2022-01-26 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0004_remove_student_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='studentemail',
            new_name='student_email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='studentid',
            new_name='student_id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='studentname',
            new_name='student_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='studentpass',
            new_name='student_password',
        ),
    ]
