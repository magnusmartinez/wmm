# Generated by Django 4.2.3 on 2023-08-07 01:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualification', '0006_remove_qualification_month_qualification_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='final_work',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='El valor debe ser mayor o igual a 0.0'), django.core.validators.MaxValueValidator(limit_value=30.0, message='El valor debe ser menor o igual a 30.0')], verbose_name='Trabajo final'),
        ),
    ]
