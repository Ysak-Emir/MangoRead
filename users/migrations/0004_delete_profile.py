# Generated by Django 4.1.4 on 2023-01-10 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_nickname_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
