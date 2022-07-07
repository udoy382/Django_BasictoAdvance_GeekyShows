# Generated by Django 4.0 on 2022-01-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0006_alter_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_email',
            field=models.EmailField(max_length=70),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(default=True, max_length=100),
        ),
    ]
