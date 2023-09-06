# Generated by Django 4.2.3 on 2023-08-07 02:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_reportcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportcode',
            name='code',
        ),
        migrations.AddField(
            model_name='reportcode',
            name='consecutive',
            field=models.CharField(default=None, editable=False, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reportcode',
            name='generation',
            field=models.CharField(default='G1-RPT-', editable=False, max_length=7),
        ),
        migrations.CreateModel(
            name='Consecutive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consecutive', models.IntegerField(default=10000001, editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='consecutive_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'consecutives',
                'db_table': 'consecutive',
            },
        ),
    ]