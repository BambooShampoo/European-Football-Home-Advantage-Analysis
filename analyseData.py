"""
    This Program takes each leagues results,goals_for,goals_against,xG_for, and xG_against for home and away. 
    It will then analyse the average of each metric across the whole season to see if those averages are equal for
    home and away.

    It will then export all those results as well as some relavant data split between home and away into one CSV for each
    League. 
"""

import sys
import os
import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt

def process_team_stats(team_name, league_df, year, leagueName):
    # Read the team match data from a CSV file
    team_match_df = pd.read_csv(f"data/{leagueName}_{year}/{team_name}_Matches_{year}.csv")
    team_match_df = team_match_df.dropna(subset=['result', 'goals_for', 'goals_against', 'xG_for', 'xG_against'])

    # Filter home and away records
    homeRecord = team_match_df[team_match_df['side'] == 'h']
    awayRecord = team_match_df[team_match_df['side'] == 'a']
    
    # Apply statistical tests
    points_pvalue = stats.ttest_ind(homeRecord['result'], awayRecord['result']).pvalue
    goals_for_pvalue = stats.ttest_ind(homeRecord['goals_for'], awayRecord['goals_for']).pvalue
    goals_against_pvalue = stats.ttest_ind(homeRecord['goals_against'], awayRecord['goals_against']).pvalue
    xG_for_pvalue = stats.ttest_ind(homeRecord['xG_for'], awayRecord['xG_for']).pvalue
    xG_against_pvalue = stats.ttest_ind(homeRecord['xG_against'], awayRecord['xG_against']).pvalue

    # save actual values
    num_games = homeRecord['result'].count()
    points = team_match_df['result'].sum()
    points_h = homeRecord['result'].sum()
    points_a = awayRecord['result'].sum()
    goals_per90_h = homeRecord['goals_for'].sum()/num_games
    goals_per90_a = awayRecord['goals_for'].sum()/num_games
    against_per90_h = homeRecord['goals_against'].sum()/num_games
    against_per90_a = awayRecord['goals_against'].sum()/num_games
    xG_per90_h = homeRecord['xG_for'].sum()/num_games
    xG_per90_a = awayRecord['xG_for'].sum()/num_games
    xGa_per90_h = homeRecord['xG_against'].sum()/num_games
    xGa_per90_a = awayRecord['xG_against'].sum()/num_games

    # Return the p-values as a dictionary
    return {
        'points': points,
        'points_h': points_h,
        'points_a': points_a,
        'goals_per90_h': goals_per90_h,
        'goals_per90_a': goals_per90_a,
        'against_per90_h': against_per90_h,
        'against_per90_a': against_per90_a,
        'xG_per90_h': xG_per90_h,
        'xG_per90_a': xG_per90_a,
        'xGa_per90_h' : xGa_per90_h,
        'xGa_per90_a': xGa_per90_a,
        'points_pvalue': points_pvalue,
        'goals_for_pvalue': goals_for_pvalue,
        'goals_against_pvalue': goals_against_pvalue,
        'xG_for_pvalue': xG_for_pvalue,
        'xG_against_pvalue': xG_against_pvalue
    }

def main(year):
    LEAGUELIST = ['Bundesliga','EPL','La_Liga','Ligue_1','Serie_A']

    for leagueName in LEAGUELIST:
        # Read the league data
        league_df = pd.read_csv(f"data/{year}/{leagueName}-{year}.csv")

        # Function to apply to each row of league_df
        def get_pvalues_for_team(row):
            team_name = row['team_title']
            team_results = process_team_stats(team_name, league_df, year, leagueName)
            return pd.Series(team_results)

        # Apply the function to each row (team) in league_df
        pvalues_df = league_df.apply(get_pvalues_for_team, axis=1)

        # Concatenate the p-values to the original league_df
        league_df = pd.concat([league_df, pvalues_df], axis=1)
        league_df = league_df[['team_title','points','points_h','points_a','goals_per90_h',
                            'goals_per90_a','against_per90_h','against_per90_a','xG_per90_h',
                            'xG_per90_a','xGa_per90_h','xGa_per90_a','points_pvalue','goals_for_pvalue',
                            'goals_against_pvalue','xG_for_pvalue','xG_against_pvalue']]

        # Sort by points in descending order
        league_df = league_df.sort_values(by='points', ascending=False)

        # Create the position column (starting from 1)
        league_df['position'] = np.arange(1, len(league_df) + 1)

        # Set the position column as the index
        league_df.set_index('position', inplace=True)

        # Define the folder where you want to save the CSV file
        folder_path = (f'data/{leagueName}_{year}/pvalue')

        # Check if the folder exists, if not, create it
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Define the file path including the folder
        file_path = os.path.join(folder_path, f"{leagueName}_{year}_with_pvalues.csv")

        # Save the DataFrame to a csv to the specified folder 
        league_df.to_csv(file_path)

        print(f"{leagueName} stats for {year}/{(int(year) + 1)} saved to {file_path}")

if __name__ == '__main__':
    year = sys.argv[1]
    main(year)
