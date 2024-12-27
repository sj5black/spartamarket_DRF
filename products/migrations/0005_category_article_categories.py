# Generated by Django 4.2 on 2024-12-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_article_author_nickname_comment_author_nickname"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="article",
            name="categories",
            field=models.ManyToManyField(blank=True, to="products.category"),
        ),
    ]