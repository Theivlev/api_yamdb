from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название категории')
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Конвертор пути')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Имя')
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Конвертор пути')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'{self.title} {self.genre}'


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Названия произведения')
    year = models.IntegerField(db_index=True)
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True)
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        verbose_name='Жанр')
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='categories',
        verbose_name='Категория')

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, verbose_name='Произведение')
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, verbose_name='Отзыв')


class Review(models.Model):
    text = models.TextField(
        verbose_name='Текст отзыва')
    score = models.IntegerField(
        validators=[MinValueValidator(1, 'Минимальная оценка 1'),
                    MaxValueValidator(10, 'Максимальная оценка 10')],
        verbose_name='рейтинг')

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',)
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'], name='unique_title_author')]


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Текст комментария')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text
