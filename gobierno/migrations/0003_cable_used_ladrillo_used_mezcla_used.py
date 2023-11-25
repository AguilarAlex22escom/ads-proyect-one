# Generated by Django 4.2.7 on 2023-11-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gobierno", "0002_cable_ladrillo_mezcla"),
    ]

    operations = [
        migrations.AddField(
            model_name="cable",
            name="used",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name="ladrillo",
            name="used",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name="mezcla",
            name="used",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]