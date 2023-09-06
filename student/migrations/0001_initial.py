# Generated by Django 4.2.3 on 2023-08-02 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('code', models.CharField(default=utils.utils.generate_random_code, max_length=7, unique=True)),
                ('grade', models.CharField(blank=True, choices=[('N/A', 'No agignado'), ('S1A', 'Primero A'), ('S1B', 'Primero B'), ('S1C', 'Primero C'), ('S2A', 'Segundo A'), ('S2B', 'Segundo B'), ('S2C', 'Segundo C'), ('S3A', 'Tercero A'), ('S3B', 'Tercero B'), ('S3C', 'Tercero C'), ('S4A', 'Cuarto A'), ('S4B', 'Cuarto B'), ('S4C', 'Cuarto C'), ('S5A', 'Quinto A'), ('S5B', 'Quinto B'), ('S5C', 'Quinto C'), ('S6A', 'Sexto A'), ('S6B', 'Sexto B'), ('S6C', 'Sexto C')], default='N/A', max_length=3, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='student_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'students',
                'db_table': 'student',
            },
        ),
    ]
