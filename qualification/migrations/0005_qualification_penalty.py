# Generated by Django 4.2.3 on 2023-08-02 22:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualification', '0004_remove_evaluationcriteria_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualification',
            name='penalty',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='El valor debe ser mayor o igual a 0.0'), django.core.validators.MaxValueValidator(limit_value=30.0, message='El valor debe ser menor o igual a 30.0')], verbose_name='Penalización'),
        ),
    ]
