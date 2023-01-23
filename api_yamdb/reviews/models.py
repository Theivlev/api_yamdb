from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import CustomUser
# Временная модель юзер
User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Category name')
    slug = models.SlugField(
        max_length=50,
        unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Genre name')
    slug = models.SlugField(
        max_length=50,
        unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Title name')
    year = models.IntegerField(db_index=True)
    description = models.TextField(
        blank=True,
        null=True)
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle')
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='categories')

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)


class Review(models.Model):
    text = models.TextField(
        verbose_name='Text review')
    score = models.IntegerField(
        validators=[MinValueValidator(1, 'Минимальная оценка 1'),
                    MaxValueValidator(10, 'Максимальная оценка 10')],
        verbose_name='Score')
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Title',)
    # пришлось взять модель User из джанги:
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Author',)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'], name='unique_title_author')]