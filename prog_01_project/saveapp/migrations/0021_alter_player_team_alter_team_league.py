# Generated by Django 5.0.1 on 2024-01-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saveapp', '0020_league_date_create_league_date_update_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='team',
            name='league',
            field=models.CharField(default='', max_length=20),
        ),
    ]