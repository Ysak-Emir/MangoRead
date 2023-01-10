from django.db import models

from users.models import User


class Genres(models.Model):
    genres_title = models.CharField(max_length=100, blank=False, verbose_name="Жанр")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.genres_title


class GenreType(models.Model):
    genre = models.ManyToManyField(Genres, through="Card")
    type_title = models.CharField(max_length=100, blank=False, verbose_name="Тип жанра")

    class Meta:
        verbose_name = "Тип жанра"
        verbose_name_plural = "Тип жанр"

    def __str__(self):
        return self.type_title


class Card(models.Model):
    profile_picture = models.ImageField(upload_to="mango_data/profile_picture", null=True, blank=False,
                                        verbose_name="Картинка")
    title = models.CharField(max_length=100, blank=False, verbose_name="Название манги")
    year = models.IntegerField(max_length=3000, blank=False, verbose_name="Год")
    description = models.TextField(null=True, blank=False, verbose_name="Описание")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE, verbose_name="Жанр")
    genres_type = models.ForeignKey(GenreType, on_delete=models.CASCADE, verbose_name="Тип жанра")
    is_puplished = models.BooleanField(default=True, verbose_name="Публикация")

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"
        ordering = ['title', 'time_create']

    def __str__(self):
        return self.title


class Review(models.Model): #Отзыв
    text = models.TextField(null=True, blank=False, verbose_name="Текст")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    mango = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name="Манго")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['time_create', 'user']

    def __str__(self):
        return self.user
