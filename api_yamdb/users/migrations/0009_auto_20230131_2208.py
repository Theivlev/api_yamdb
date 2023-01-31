# Generated by Django 3.2 on 2023-01-31 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_customuser_username'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='customuser',
            name='unique_fields',
        ),
        migrations.AddConstraint(
            model_name='customuser',
            constraint=models.UniqueConstraint(fields=('username',), name='unique_fields'),
        ),
    ]