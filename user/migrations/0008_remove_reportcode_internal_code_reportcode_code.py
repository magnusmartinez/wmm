# Generated by Django 4.2.3 on 2023-08-31 03:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_reportcode_code_reportcode_internal_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportcode',
            name='internal_code',
        ),
        migrations.AddField(
            model_name='reportcode',
            name='code',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
