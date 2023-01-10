# Generated by Django 4.1.4 on 2023-01-07 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mango', '0011_alter_review_mango_alter_review_text_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['title', 'time_create'], 'verbose_name': 'Карточка', 'verbose_name_plural': 'Карточки'},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='genretype',
            options={'verbose_name': 'Тип жанра', 'verbose_name_plural': 'Тип жанр'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['time_create', 'user'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]