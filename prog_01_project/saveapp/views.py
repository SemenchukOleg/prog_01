from django.shortcuts import render, redirect
import requests

from saveapp.models import Leagues
import pandas as pd
# Create your views here.


def reload_data(request):
    BASE_URL = 'https://api.football-data.org/v4/competitions/'
    leagues_code = ['PL', 'PD', 'BL1']
    API_KEY = '11d7150bbd094f9ab05b0c535a5bf89c'
    headers = {'X-Auth-Token': API_KEY}
    seasons = ['2020', '2021', '2022']

    for league_code in leagues_code:
        for season in seasons:
            filter = {'season': season}
            teams_response = requests.get(BASE_URL + league_code + '/teams', headers=headers, params=filter)
            table_row_data = teams_response.json()

            #возвращает котреж (obj, False) или создает объект лиги 
            league = Leagues.objects.get_or_create(
                legue_id = table_row_data['competition']['id'],
                league = table_row_data['competition']['name'],
                league_code = table_row_data['competition']['code'],
                league_emblem = table_row_data['competition']['emblem'],
                )
            
            for team in table_row_data['teams']:
                #создает команду привязанную к лиге
                team_create = league[0].teams_set.get_or_create(
                    team_id = team['id'],
                    team_name = team['name'],
                    team_website = team['website'],
                    team_emblem = team["crest"],
                    season = season,    
                )
                for person in team['squad']:
                    #создает игрока привязанного к команде
                    team_create[0].players_set.get_or_create(
                        player_id = person['id'],
                        name = person['name'],
                        position = person['position'],
                        date_of_birth = pd.to_datetime(person['dateOfBirth']),
                        nationality = person['nationality'],
                        season = season,
                    )

                
        
    return redirect('admin/')

