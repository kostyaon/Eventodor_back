# Generated by Django 4.0.2 on 2022-02-17 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventodor_back', '0008_event_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
    ]