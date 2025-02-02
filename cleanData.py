"""
    This program takes the data from gatherData.py as well as match data for each team in each league for the year.
    It will then export the Team name, and for each game how many points they recorded, what side they are on, how many goals they scored,
    how many they conceided, their expected goals, and expected goals against.

    The export will be a csv file for each team stored in a folder for that league_year
"""

import sys
import os
import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt
from understatapi import UnderstatClient

def main(year):


    understat = UnderstatClient()

    LEAGUELIST = ['Bundesliga','EPL','La_Liga','Ligue_1','Serie_A']

    for leagueName in LEAGUELIST:
        # Define the folder where you want to save the CSV file
        leagueDF = pd.read_csv(f'data/{year}/{leagueName}-{year}.csv')
        folder_path = (f"data/{leagueName}_{year}")

        # Check if the folder exists, if not, create it
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Loop through each team
        for team_name in leagueDF["team_title"]:
            # Call the API for the current team
            team_data = understat.team(team=team_name).get_match_data(season=year)
            teamMatches = pd.DataFrame(team_data)

            numeric_cols = ['id', 'isResult', 'side', 'h', 'a', 'goals', 'xG', 'datetime', 'forecast', 'result']
            teamMatches[numeric_cols] = teamMatches[numeric_cols]

            # Convert 'result' column from 'l', 'd', 'w' to 0, 1, 3
            result_mapping = {'l': 0, 'd': 1, 'w': 3}
            teamMatches['result'] = teamMatches['result'].map(result_mapping)

            # clean the data a little more
            teamMatches['goals_for'] = teamMatches.apply(lambda game: game['goals']['a'] if game['side'] == 'a' else game['goals']['h'], axis=1)
            teamMatches['goals_against'] = teamMatches.apply(lambda game: game['goals']['h'] if game['side'] == 'a' else game['goals']['a'], axis=1)
            teamMatches['xG_for'] = teamMatches.apply(lambda game: game['xG']['a'] if game['side'] == 'a' else game['xG']['h'], axis=1)
            teamMatches['xG_against'] = teamMatches.apply(lambda game: game['xG']['h'] if game['side'] == 'a' else game['xG']['a'], axis=1)

            teamMatches = teamMatches.drop(columns=['isResult','h', 'a','goals','xG','datetime','forecast'], errors='ignore')

            # Define the file path including the folder
            file_path = os.path.join(folder_path, team_name+"_Matches_"+ year +".csv")

            # Save the DataFrame to the specified folder
            teamMatches.to_csv(file_path)

            print(f"{team_name} match Data for {year}/{(int(year) + 1)} saved to {file_path}")

    

    
if __name__=='__main__':
    year = sys.argv[1]
    main(year)