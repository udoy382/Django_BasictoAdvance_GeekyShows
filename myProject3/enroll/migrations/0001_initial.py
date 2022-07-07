# Generated by Django 4.0 on 2022-01-26 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.IntegerField(max_length=50)),
                ('studentname', models.CharField(max_length=70)),
                ('studentemail', models.EmailField(max_length=254)),
                ('studentpass', models.CharField(max_length=70)),
            ],
        ),
    ]
