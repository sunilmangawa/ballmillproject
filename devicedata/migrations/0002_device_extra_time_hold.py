# Generated by Django 4.2 on 2023-05-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devicedata", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="extra_time_hold",
            field=models.IntegerField(default=0),
        ),
    ]