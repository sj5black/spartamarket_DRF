# Generated by Django 4.2 on 2024-12-27 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="author",
            new_name="author_id",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="author",
            new_name="author_id",
        ),
    ]