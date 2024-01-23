from django.contrib import admin
from saveapp.models import League, Team, Player

class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_update')

class TeamAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('league', 'season')


class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name', 'position', 'date_of_birth', 'nationality')
    list_display = ('name', 'position', 'date_of_birth', 'nationality', 'team')
    list_filter = ('position', 'nationality', 'team', 'season')


# Register your models here.

admin.site.register(League, LeagueAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)


