# Generated by Django 4.1.5 on 2023-06-07 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("EpiceneApp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="Action",
        ),
        migrations.RemoveField(
            model_name="event",
            name="Action_date",
        ),
        migrations.RemoveField(
            model_name="event",
            name="Reject_reason",
        ),
    ]