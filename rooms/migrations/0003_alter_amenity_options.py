# Generated by Django 4.2.17 on 2025-01-27 16:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0002_room_name_alter_amenity_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="amenity",
            options={"verbose_name_plural": "Amenities"},
        ),
    ]
