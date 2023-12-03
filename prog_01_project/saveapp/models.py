from django.db import models
from django.contrib import admin

# Create your models here.

class Leagues(models.Model):
    legue_id = models.IntegerField(default=0)
    league = models.CharField(max_length=20, default='')
    league_code = models.CharField(max_length=5, default='')
    league_emblem = models.URLField(default='')

    def __str__(self):
        return self.league
    



class Teams(models.Model):
    team_id = models.IntegerField(default=0)
    team_name = models.CharField(max_length=20, default='')
    team_emblem = models.URLField(default='')
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE, default=0)
    team_website = models.URLField(default='')
    season = models.IntegerField(blank=True, null=True, default=0)
    def __str__(self):
        return self.team_name





class Players(models.Model):
    player_id = models.IntegerField(default=0)
    name = models.CharField(max_length=30, default='')
    position = models.CharField(max_length=20, default='')
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=20, default='')
    season = models.IntegerField(blank=True, null=True, default=0)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.name
