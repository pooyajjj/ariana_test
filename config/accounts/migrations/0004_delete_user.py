# Generated by Django 4.2 on 2023-04-24 16:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_user_is_staff"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
