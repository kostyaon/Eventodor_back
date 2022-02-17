# Generated by Django 4.0.2 on 2022-02-17 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventodor_back', '0005_remove_user_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='events',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eventodor_back.event'),
            preserve_default=False,
        ),
    ]
