# Generated by Django 5.2.2 on 2025-06-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_tags_tags_choices_save'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiers_choices_save', models.CharField(choices=[('S+', 'S+'), ('S', 'S'), ('A+', 'A+'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='cardata',
            name='tags_choices_save',
        ),
        migrations.RemoveField(
            model_name='cardata',
            name='tier',
        ),
        migrations.AddField(
            model_name='cardata',
            name='car_power',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cardata',
            name='car_tag',
            field=models.CharField(blank=True, choices=[('HYPER CAR', 'HYPER CAR'), ('SUPER CAR', 'SUPER CAR'), ('SPORT CAR', 'SPORT CAR'), ('MUSCLE CAR', 'MUSCLE CAR'), ('LUXURY CAR', 'LUXURY CAR'), ('COLLECTIBLE CAR', 'COLLECTIBLE CAR'), ('RACE CAR', 'RACE CAR'), ('COMMON CAR', 'COMMON CAR'), ('OTHERS', 'OTHERS')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cardata',
            name='car_tier',
            field=models.CharField(blank=True, choices=[('S+', 'S+'), ('S', 'S'), ('A+', 'A+'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='cardata',
            name='car_torque',
            field=models.IntegerField(null=True),
        ),
    ]
