# Generated by Django 4.2 on 2024-12-28 05:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0006_category_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="like_users",
            field=models.ManyToManyField(
                blank=True, related_name="like_articles", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
