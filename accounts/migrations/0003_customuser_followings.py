# Generated by Django 4.2 on 2024-12-27 17:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "accounts",
            "0002_alter_customuser_birth_date_alter_customuser_email_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="followings",
            field=models.ManyToManyField(
                blank=True, related_name="followers", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
