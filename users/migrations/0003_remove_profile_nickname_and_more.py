# Generated by Django 4.1.4 on 2023-01-10 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]