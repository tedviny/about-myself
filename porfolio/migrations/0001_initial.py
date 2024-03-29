# Generated by Django 4.2.10 on 2024-02-27 21:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MessageContact",
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
                ("email", models.EmailField(max_length=40, verbose_name="email")),
                ("message", models.TextField(verbose_name="message")),
                ("date", models.DateTimeField(null="TRUE", verbose_name="date")),
            ],
            options={
                "ordering": ["date"],
            },
        ),
        migrations.CreateModel(
            name="UserContact",
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
                ("email", models.EmailField(max_length=40, verbose_name="email")),
            ],
        ),
    ]
