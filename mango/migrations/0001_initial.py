# Generated by Django 4.1.4 on 2023-01-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(null=True, upload_to='mango_data/profile_picture', verbose_name='Картинка')),
                ('title', models.CharField(max_length=100, verbose_name='Название манги')),
                ('year', models.IntegerField(max_length=3000, verbose_name='Год')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Карточка',
                'verbose_name_plural': 'Карточка',
                'ordering': ['title', 'year'],
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres_title', models.CharField(max_length=100, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанры',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='GenreType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_title', models.CharField(max_length=100, verbose_name='Тип жанра')),
            ],
            options={
                'verbose_name': 'Тип жанра',
                'verbose_name_plural': 'Тип жанра',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]