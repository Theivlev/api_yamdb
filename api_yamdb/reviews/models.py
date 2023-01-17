from django.db import models


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
        related_name='categories'
    )

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
