# Generated by Django 4.2.3 on 2023-07-19 00:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("peliculas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pelicula",
            name="release",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Lanzamiento"
            ),
        ),
    ]
