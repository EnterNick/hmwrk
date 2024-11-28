# Generated by Django 5.1.3 on 2024-11-28 10:54

import app.models
import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='price',
        ),
        migrations.AddField(
            model_name='good',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='good',
            name='date_created',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='good',
            name='ingredients',
            field=models.JSONField(default=app.models.default_list),
        ),
        migrations.AddField(
            model_name='good',
            name='instruction',
            field=models.TextField(blank=True, null=True),
        ),
    ]
