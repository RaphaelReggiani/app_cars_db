# Generated by Django 5.2.2 on 2025-06-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_alter_cardata_car_tier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tier',
            name='tiers_choices_save',
            field=models.CharField(choices=[('S+', 'S+'), ('S', 'S'), ('A+', 'A+'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=10),
        ),
    ]
