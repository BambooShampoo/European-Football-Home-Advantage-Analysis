"""
This program collects data from the understatApi for each league in the argument year, it will then group the data to collect some metrics and 
team information for that year.

it will then export it as seperate csv files for each league in a folder of that year.
"""

import sys
import os
import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt
from understatapi import UnderstatClient

def main(year):

    LEAGUELIST = ['Bundesliga','EPL','La_Liga','Ligue_1','Serie_A']
    understat = UnderstatClient()

    # Define the folder where you want to save the CSV file
    folder_path = (f"data/{year}")

    # Check if the folder exists, if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for league in LEAGUELIST:
        # get the data from api
        leagueData = understat.league(league=league).get_player_data(season=year)

        # take raw data
        Playerdata = pd.DataFrame(leagueData)

        # clean it up
        numeric_cols = ['games', 'time', 'goals', 'xG', 'assists', 'xA', 'shots', 'key_passes', 'yellow_cards', 'red_cards', 'npg', 'npxG', 'xGChain', 'xGBuildup']
        Playerdata[numeric_cols] = Playerdata[numeric_cols].apply(pd.to_numeric)

        # make team data for that season
        grouped = Playerdata.groupby('team_title').sum()

        # Replace spaces with underscores in the index
        grouped.index = grouped.index.str.replace(' ', '_')

        # Filter out rows where team_title (index) contains a comma
        cleaned = grouped[~grouped.index.str.contains(',', na=False)]

        # Drop 'player_name' and 'position' columns
        cleaned = cleaned.drop(columns=['id','player_name', 'position'], errors='ignore')

        # Define the file path including the folder
        file_path = os.path.join(folder_path, league+"-"+year+".csv")

        # Save to CSV in the year folder
        cleaned.to_csv(file_path)

        print(f"{league} Data for {year}/{(int(year) + 1)} saved to {file_path}")
    

    
if __name__=='__main__':
    year = sys.argv[1]
    main(year)