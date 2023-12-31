# Generated by Django 4.2.3 on 2023-08-02 21:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualification', '0003_punctuationcriteria_punctuation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluationcriteria',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='punctuation',
            name='evaluation',
        ),
        migrations.RemoveField(
            model_name='punctuation',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='punctuation',
            name='values',
        ),
        migrations.RemoveField(
            model_name='punctuationcriteria',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='qualification',
            name='evaluation',
        ),
        migrations.AddField(
            model_name='qualification',
            name='exercise',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='El valor debe ser mayor o igual a 0.0'), django.core.validators.MaxValueValidator(limit_value=5.0, message='El valor debe ser menor o igual a 5.0')], verbose_name='Ejercicios'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='final_work',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='El valor debe ser mayor o igual a 0.0'), django.core.validators.MaxValueValidator(limit_value=30.0, message='El valor debe ser menor o igual a 30.0')], verbose_name='Producto final'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='notebook_note',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='El valor debe ser mayor o igual a 0.0'), django.core.validators.MaxValueValidator(limit_value=10.0, message='El valor debe ser menor o igual a 10.0')], verbose_name='Cuaderno'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='participation_note',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='El valor debe ser mayor o igual a 0.0'), django.core.validators.MaxValueValidator(limit_value=20.0, message='El valor debe ser menor o igual a 20.0')], verbose_name='Participación'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='practice',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='El valor debe ser mayor o igual a 0.0'), django.core.validators.MaxValueValidator(limit_value=5.0, message='El valor debe ser menor o igual a 5.0')], verbose_name='Prácticas'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='presentation',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='El valor debe ser mayor o igual a 0.0'), django.core.validators.MaxValueValidator(limit_value=30.0, message='El valor debe ser menor o igual a 30.0')], verbose_name='Exposiciones'),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='value',
            field=models.FloatField(blank=True, editable=False, null=True, verbose_name='Calificación mensual acomulada'),
        ),
        migrations.DeleteModel(
            name='Evaluation',
        ),
        migrations.DeleteModel(
            name='EvaluationCriteria',
        ),
        migrations.DeleteModel(
            name='Punctuation',
        ),
        migrations.DeleteModel(
            name='PunctuationCriteria',
        ),
    ]
