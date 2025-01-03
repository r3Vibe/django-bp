# Generated by Django 5.1.2 on 2024-12-13 09:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_historicaluser"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicaluser",
            name="created_at",
            field=models.DateTimeField(
                blank=True, default=django.utils.timezone.now, editable=False
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
