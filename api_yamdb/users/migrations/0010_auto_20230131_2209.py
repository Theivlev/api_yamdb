# Generated by Django 3.2 on 2023-01-31 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20230131_2208'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveConstraint(
            model_name='customuser',
            name='unique_fields',
        ),
    ]