# Generated by Django 4.2.1 on 2023-05-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("Isbn", models.CharField(max_length=100)),
                ("publisher", models.CharField(max_length=100)),
            ],
        ),
    ]