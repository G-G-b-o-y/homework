# Generated by Django 5.1.6 on 2025-04-04 09:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_modelpost"),
    ]

    operations = [
        migrations.CreateModel(
            name="WeatherData",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("minTemp", models.IntegerField()),
                ("maxTemp", models.IntegerField()),
                ("weather_type", models.CharField(max_length=30)),
                ("rain_probability", models.IntegerField()),
            ],
        ),
    ]
