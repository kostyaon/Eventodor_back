# Generated by Django 4.0.2 on 2022-02-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventodor_back', '0010_userevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000)),
            ],
        ),
    ]