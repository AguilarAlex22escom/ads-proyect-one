# Generated by Django 4.2.7 on 2023-11-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gobierno", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cable",
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
                (
                    "name",
                    models.CharField(
                        default="Cable", editable=False, max_length=16, unique=True
                    ),
                ),
                ("quantity", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Cable",
                "verbose_name_plural": "Listado de cable",
            },
        ),
        migrations.CreateModel(
            name="Ladrillo",
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
                (
                    "name",
                    models.CharField(
                        default="Ladrillo", editable=False, max_length=16, unique=True
                    ),
                ),
                ("quantity", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Ladrillo",
                "verbose_name_plural": "Listado de Ladrillos",
            },
        ),
        migrations.CreateModel(
            name="Mezcla",
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
                (
                    "name",
                    models.CharField(
                        default="Mezcla", editable=False, max_length=16, unique=True
                    ),
                ),
                ("quantity", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Mezcla",
                "verbose_name_plural": "Listado de mezcla",
            },
        ),
    ]
