# Generated by Django 5.2.2 on 2025-07-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0023_cars_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='reset_token',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
