# Generated by Django 4.2.3 on 2023-08-30 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qualification', '0008_alter_qualification_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementIndicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='achievement_indicator_user', to=settings.AUTH_USER_MODEL, verbose_name='Docente')),
            ],
            options={
                'verbose_name_plural': 'Achievement Indicators',
                'db_table': 'achievement_indicator',
            },
        ),
        migrations.CreateModel(
            name='FundamentalCompetencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('achievement_indicators', models.ManyToManyField(to='qualification.achievementindicator')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fundamental_competencies_user', to=settings.AUTH_USER_MODEL, verbose_name='Docente')),
            ],
            options={
                'verbose_name_plural': 'Fundamental competencies',
                'db_table': 'fundamental_competencies',
            },
        ),
        migrations.AddField(
            model_name='qualification',
            name='achievement_indicators',
            field=models.ManyToManyField(to='qualification.achievementindicator'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='fundamental_competencies',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='qualification.fundamentalcompetencies'),
            preserve_default=False,
        ),
    ]
