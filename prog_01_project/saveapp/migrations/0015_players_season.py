# Generated by Django 4.2.7 on 2023-12-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saveapp', '0014_alter_teams_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='season',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
