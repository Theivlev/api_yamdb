from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    USER_ROLES = [
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    ]
    username = models.CharField(
        max_length=140,
        blank=False,
        null=True,
        unique=True,)
    email = models.EmailField(('email address'), unique=True, max_length=200,)
    role = models.CharField(
        verbose_name='Роль пользователя',
        max_length=25,
        choices=USER_ROLES,
        default='user',
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Биография')

    def __str__(self):
        return self.username

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN
