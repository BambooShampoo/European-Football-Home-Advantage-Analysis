import sys
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def process_team_stats(team_name, league_df, year, leagueName):
    # Read the team match data from a CSV file
    team_match_df = pd.read_csv(f"data/{leagueName}_{year}/{team_name}_Matches_{year}.csv")
    team_match_df = team_match_df.dropna(subset=['result', 'goals_for', 'goals_against', 'xG_for', 'xG_against'])
    # Filter home and away records
    homeRecord = team_match_df[team_match_df['side'] == 'h']
    awayRecord = team_match_df[team_match_df['side'] == 'a']
    
    # Plot histograms for points, goals for, goals against, xG for, xG against
    save_histograms(team_name, homeRecord, awayRecord, leagueName, year)

    # Return the actual values (for potential further use)
    return homeRecord, awayRecord

def save_histograms(team_name, homeRecord, awayRecord, leagueName, year):
    # Create subplots for each stat
    fig, plot = plt.subplots(3, 2, figsize=(12, 12))
    bin_size = 12
    # Plot Points side-by-side histogram
    plot[0, 0].hist([homeRecord['result'], awayRecord['result']], bins=bin_size, label=['Home', 'Away'], color=['lightblue', 'lightcoral'], edgecolor='black', alpha=0.7)
    plot[0, 0].set_title(f'{team_name} - Points Recorded in a game(Home vs Away)')
    plot[0, 0].set_xlabel('Points')
    plot[0, 0].set_ylabel('Frequency')
    plot[0, 0].legend()

    # Plot Goals For side-by-side histogram
    plot[0, 1].hist([homeRecord['goals_for'], awayRecord['goals_for']], bins=bin_size, label=['Home', 'Away'], color=['lightblue', 'lightcoral'], edgecolor='black', alpha=0.7)
    plot[0, 1].set_title(f'{team_name} - Goals Scored in a game (Home vs Away)')
    plot[0, 1].set_xlabel('Goals For')
    plot[0, 1].set_ylabel('Frequency')
    plot[0, 1].legend()

    # Plot Goals Against side-by-side histogram
    plot[1, 0].hist([homeRecord['goals_against'], awayRecord['goals_against']], bins=bin_size, label=['Home', 'Away'], color=['lightblue', 'lightcoral'], edgecolor='black', alpha=0.7)
    plot[1, 0].set_title(f'{team_name} - Goals Concieded in a game (Home vs Away)')
    plot[1, 0].set_xlabel('Goals Against')
    plot[1, 0].set_ylabel('Frequency')
    plot[1, 0].legend()

    # Plot xG For side-by-side histogram
    plot[1, 1].hist([homeRecord['xG_for'], awayRecord['xG_for']], bins=bin_size, label=['Home', 'Away'], color=['lightblue', 'lightcoral'], edgecolor='black', alpha=0.7)
    plot[1, 1].set_title(f'{team_name} - Expected Goals in a game (Home vs Away)')
    plot[1, 1].set_xlabel('xG For')
    plot[1, 1].set_ylabel('Frequency')
    plot[1, 1].legend()

    # Plot xG Against side-by-side histogram
    plot[2, 0].hist([homeRecord['xG_against'], awayRecord['xG_against']], bins=bin_size, label=['Home', 'Away'], color=['lightblue', 'lightcoral'], edgecolor='black', alpha=0.7)
    plot[2, 0].set_title(f'{team_name} - Expected Goals Against in a game (Home vs Away)')
    plot[2, 0].set_xlabel('xG Against')
    plot[2, 0].set_ylabel('Frequency')
    plot[2, 0].legend()

    # Hide the unused subplot
    plot[2, 1].axis('off')

    # Save the figure as an image file in the pvalue folder
    folder_path = os.path.join(f'{leagueName}_{year}/histograms')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Save as PNG file
    file_path = os.path.join(folder_path, f"{team_name}_histograms.png")
    plt.tight_layout()
    plt.savefig(file_path)
    print(f"Histograms for {team_name} saved to {file_path}")
    
    # Close the plot to free up memory
    plt.close(fig)

def main(leagueName, year):
    # Read the league data
    league_df = pd.read_csv(f"{year}/{leagueName}-{year}.csv")

    # Function to apply to each row of league_df
    def get_histograms_for_team(row):
        team_name = row['team_title']
        process_team_stats(team_name, league_df, year, leagueName)

    # Apply the function to each row (team) in league_df
    league_df.apply(get_histograms_for_team, axis=1)

if __name__ == '__main__':
    leagueName = sys.argv[1]
    year = sys.argv[2]
    main(leagueName, year)
