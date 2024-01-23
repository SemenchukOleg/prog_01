import pandas as pd
import requests
from django.shortcuts import redirect, render
from saveapp.models import League, Team, Player

from prog_01_project.settings import API_KEY

# Create your views here.



def reload_data(request):
    BASE_URL = 'https://api.football-data.org/v4/competitions/'
    headers = {'X-Auth-Token': API_KEY}
    #seasons = ['2020', '2021', '2022']
    leagues_code = ['PL', 'PD', 'BL1']
    print (request.POST)
    season = request.POST['season']
    
    filter = {'season': season}
    PL_teams_response = requests.get(BASE_URL + 'PL/teams', headers=headers, params=filter)
    PL_table_row_data = PL_teams_response.json()
    PD_teams_response = requests.get(BASE_URL + 'PD/teams', headers=headers, params=filter)
    PD_table_row_data = PD_teams_response.json()
    BL1_teams_response = requests.get(BASE_URL + 'BL1/teams', headers=headers, params=filter)
    BL1_table_row_data = BL1_teams_response.json()
    ALL_table_row_data = [PL_table_row_data, PD_table_row_data, BL1_table_row_data]

    if 'Leagues' in request.POST:
        reload_league(ALL_table_row_data)
        print('лиги обновлены')
    if 'Teams' in request.POST:
        reload_team(ALL_table_row_data, season)
        print('команды обновлены')
    if 'Players' in request.POST:
        reload_player(ALL_table_row_data, season)
        print('игроки обновлены')
        

    # for league_code in leagues_code:
    #     for season in seasons:
    #         filter = {'season': season}
    #         teams_response = requests.get(BASE_URL + league_code + '/teams', headers=headers, params=filter)
    #         table_row_data = teams_response.json()

            
    #         league = League.objects.get_or_create(                       #возвращает котреж (obj, False) или создает объект лиги
    #             legue_id = table_row_data['competition']['id'],
    #             name = table_row_data['competition']['name'],
    #             league_code = table_row_data['competition']['code'],
    #             league_emblem = table_row_data['competition']['emblem'],
    #             )
            
    #         for team in table_row_data['teams']:
                
    #             team_create = league[0].teams_set.get_or_create(          #возвращает котреж (obj, False) или создает объект команды привязанной к лиге
    #                 team_id = team['id'],
    #                 name = team['name'],
    #                 team_website = team['website'],
    #                 team_emblem = team["crest"],
    #                 season = season,    
    #             )
    #             for person in team['squad']:
                    
    #                 team_create[0].players_set.get_or_create(              #возвращает котреж (obj, False) или создает объект игрока к команде
    #                     player_id = person['id'],
    #                     name = person['name'],
    #                     position = person['position'],
    #                     date_of_birth = pd.to_datetime(person['dateOfBirth']),
    #                     nationality = person['nationality'],
    #                     season = season,
    #                 )

        
    return redirect('admin/')

def reload_league (ALL_table_row_data):
    for table_row_data in ALL_table_row_data:
        League.objects.update_or_create(                       #возвращает котреж (obj, False) или создает объект лиги
        legue_id = table_row_data['competition']['id'],
        name = table_row_data['competition']['name'],
        league_code = table_row_data['competition']['code'],
        league_emblem = table_row_data['competition']['emblem'],
        )

def reload_team(ALL_table_row_data, season) :
    for table_row_data in ALL_table_row_data:
        for team in table_row_data['teams']:
            Team.objects.update_or_create(          #возвращает котреж (obj, False) или создает объект команды привязанной к лиге
                team_id = team['id'],
                name = team['name'],
                team_website = team['website'],
                team_emblem = team['crest'],
                league =  table_row_data['competition']['code'],
                season = season,    
            )

def reload_player(ALL_table_row_data, season):
    for table_row_data in ALL_table_row_data:
        for team in table_row_data['teams']:
            for person in team['squad']:                
                Player.objects.update_or_create(              #возвращает котреж (obj, False) или создает объект игрока к команде
                    player_id = person['id'],
                    name = person['name'],
                    position = person['position'],
                    date_of_birth = pd.to_datetime(person['dateOfBirth']),
                    nationality = person['nationality'],
                    season = season,
                )