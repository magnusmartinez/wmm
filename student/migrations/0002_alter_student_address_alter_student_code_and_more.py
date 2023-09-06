# Generated by Django 4.2.3 on 2023-08-02 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='student',
            name='code',
            field=models.CharField(default=utils.utils.generate_random_code, max_length=7, unique=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(blank=True, choices=[('N/A', 'No agignado'), ('S1A', 'Primero A'), ('S1B', 'Primero B'), ('S1C', 'Primero C'), ('S2A', 'Segundo A'), ('S2B', 'Segundo B'), ('S2C', 'Segundo C'), ('S3A', 'Tercero A'), ('S3B', 'Tercero B'), ('S3C', 'Tercero C'), ('S4A', 'Cuarto A'), ('S4B', 'Cuarto B'), ('S4C', 'Cuarto C'), ('S5A', 'Quinto A'), ('S5B', 'Quinto B'), ('S5C', 'Quinto C'), ('S6A', 'Sexto A'), ('S6B', 'Sexto B'), ('S6C', 'Sexto C')], default='N/A', max_length=3, null=True, verbose_name='Grado'),
        ),
        migrations.AlterField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='student',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='student_user', to=settings.AUTH_USER_MODEL, verbose_name='Profesor'),
        ),
        migrations.AlterField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización'),
        ),
    ]
