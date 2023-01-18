# Generated by Django 3.2 on 2023-01-18 15:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text review')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Минимальная оценка 1'), django.core.validators.MaxValueValidator(10, 'Максимальная оценка 10')], verbose_name='Score')),
                ('author', models.IntegerField(db_index=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.title', verbose_name='Title')),
            ],
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_title_author'),
        ),
    ]
