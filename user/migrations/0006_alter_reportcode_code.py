# Generated by Django 4.2.3 on 2023-08-31 03:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_reportcode_consecutive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcode',
            name='code',
            field=models.CharField(default=uuid.uuid4, max_length=32, unique=True),
        ),
    ]
