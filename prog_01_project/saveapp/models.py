from django.db import models
from django.contrib import admin

# Create your models here.

class League(models.Model):
    legue_id = models.IntegerField(default=0)
    name = models.CharField(max_length=20, default='')
    league_code = models.CharField(max_length=5, default='')
    league_emblem = models.URLField(default='')
    date_create = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(editable = True, auto_now = True)

    def __str__(self):
        return self.name
    



class Team(models.Model):
    team_id = models.IntegerField(default=0)
    name = models.CharField(max_length=20, default='')
    team_emblem = models.URLField(default='')
    league = models.CharField(max_length=20, default='')
    team_website = models.URLField(default='')
    season = models.IntegerField(blank=True, null=True, default=0)
    date_create = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField (editable=True, auto_now = True)

    def __str__(self):
        return self.name





class Player(models.Model):
    player_id = models.IntegerField(default=0)
    name = models.CharField(max_length=30, default='')
    position = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=20, default='', blank=True, null=True)
    season = models.IntegerField(blank=True, null=True, default=0)
    team = models.CharField(max_length=20, default='')
    date_create = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(editable = True, auto_now = True)

    def __str__(self):
        return self.name
