# Generated by Django 5.0.4 on 2024-05-15 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='user',
        ),
        migrations.RemoveField(
            model_name='master',
            name='created_user',
        ),
    ]
