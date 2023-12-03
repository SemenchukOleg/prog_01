from django.contrib import admin
from saveapp.models import Leagues, Teams, Players


class TeamsAdmin(admin.ModelAdmin):
    search_fields = ('team_name',)
    list_display = ('team_name',)
    list_filter = ('league', 'season')


class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name', 'position', 'date_of_birth', 'nationality')
    list_display = ('name', 'position', 'date_of_birth', 'nationality', 'team')
    list_filter = ('position', 'nationality', 'team', 'season')


# Register your models here.

admin.site.register(Leagues)
admin.site.register(Teams, TeamsAdmin)
admin.site.register(Players, PlayerAdmin)


