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
    
    # Plot boxplots for points, goals for, goals against, xG for, xG against
    save_boxplots(team_name, homeRecord, awayRecord, leagueName, year)

    # Return the actual values (for potential further use)
    return homeRecord, awayRecord

def save_boxplots(team_name, homeRecord, awayRecord, leagueName, year):
    # Create subplots for each stat
    fig, plot = plt.subplots(3, 2, figsize=(12, 12))

    # Plot Points horizontal boxplot
    plot[0, 0].boxplot([awayRecord['result'], homeRecord['result']], vert=False, labels=['Away','Home'], patch_artist=True)
    plot[0, 0].set_title(f'{team_name} - Points (Home vs Away)')
    plot[0, 0].set_xlabel('Points')

    # Plot Goals For horizontal boxplot
    plot[0, 1].boxplot([awayRecord['goals_for'], homeRecord['goals_for']], vert=False, labels=['Away','Home'], patch_artist=True)
    plot[0, 1].set_title(f'{team_name} - Goals For (Home vs Away)')
    plot[0, 1].set_xlabel('Goals For')

    # Plot Goals Against horizontal boxplot
    plot[1, 0].boxplot([awayRecord['goals_against'], homeRecord['goals_against']], vert=False, labels=['Away','Home'], patch_artist=True)
    plot[1, 0].set_title(f'{team_name} - Goals Against (Home vs Away)')
    plot[1, 0].set_xlabel('Goals Against')

    # Plot xG For horizontal boxplot
    plot[1, 1].boxplot([awayRecord['xG_for'], homeRecord['xG_for']], vert=False, labels=['Away','Home'], patch_artist=True)
    plot[1, 1].set_title(f'{team_name} - xG For (Home vs Away)')
    plot[1, 1].set_xlabel('xG For')

    # Plot xG Against horizontal boxplot
    plot[2, 0].boxplot([awayRecord['xG_against'], homeRecord['xG_against']], vert=False, labels=['Away','Home'], patch_artist=True)
    plot[2, 0].set_title(f'{team_name} - xG Against (Home vs Away)')
    plot[2, 0].set_xlabel('xG Against')

    # Hide the unused subplot
    plot[2, 1].axis('off')

    # Save the figure as an image file in the pvalue folder
    folder_path = os.path.join(f'{leagueName}_{year}/boxplots')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Save as PNG file
    file_path = os.path.join(folder_path, f"{team_name}_boxplots_horizontal.png")
    plt.tight_layout()
    plt.savefig(file_path)
    print(f"Horizontal Boxplots for {team_name} saved to {file_path}")
    
    # Close the plot to free up memory
    plt.close(fig)

def main(leagueName, year):
    # Read the league data
    league_df = pd.read_csv(f"{year}/{leagueName}-{year}.csv")

    # Function to apply to each row of league_df
    def get_boxplots_for_team(row):
        team_name = row['team_title']
        process_team_stats(team_name, league_df, year, leagueName)

    # Apply the function to each row (team) in league_df
    league_df.apply(get_boxplots_for_team, axis=1)

if __name__ == '__main__':
    leagueName = sys.argv[1]
    year = sys.argv[2]
    main(leagueName, year)
