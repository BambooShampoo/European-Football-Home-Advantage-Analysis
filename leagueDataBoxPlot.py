import sys
import os
import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt

def main(year):
    LEAGUELIST = ['Bundesliga','EPL','La_Liga','Ligue_1','Serie_A']

    for league in LEAGUELIST:
        # load into dataframe
        LeagueStats = pd.read_csv(f"data/{league}_{year}/pvalue/{league}_{year}_with_pvalues.csv")

        # is there a difference in each metric home vs away?
        league_points_pvalue = stats.ttest_ind(LeagueStats['points_h'], LeagueStats['points_a']).pvalue
        league_goals_for_pvalue = stats.ttest_ind(LeagueStats['goals_per90_h'], LeagueStats['goals_per90_a']).pvalue
        league_goals_against_pvalue = stats.ttest_ind(LeagueStats['against_per90_h'], LeagueStats['against_per90_a']).pvalue
        league_xG_for_pvalue = stats.ttest_ind(LeagueStats['xG_per90_h'], LeagueStats['xG_per90_a']).pvalue
        league_xG_against_pvalue = stats.ttest_ind(LeagueStats['xGa_per90_h'], LeagueStats['xGa_per90_a']).pvalue

        # adapted from dataBoxplot.py in the repo
        fig, boxPlot = plt.subplots(3, 2, figsize=(12, 12))

        # Plot Points horizontal boxplot
        boxPlot[0, 0].boxplot([LeagueStats['points_a'], LeagueStats['points_h']], vert=False, tick_labels=['Away','Home'], patch_artist=True)
        boxPlot[0, 0].set_title(f'{league} - {year}: Points Earned(Home vs Away)')
        boxPlot[0, 0].set_xlabel('Points')

        # Plot Goals For horizontal boxplot
        boxPlot[0, 1].boxplot([LeagueStats['goals_per90_a'], LeagueStats['goals_per90_h']], vert=False, tick_labels=['Away','Home'], patch_artist=True)
        boxPlot[0, 1].set_title(f'{league} - {year}: Goals Scored (Home vs Away)')
        boxPlot[0, 1].set_xlabel('Goals For')

        # Plot Goals Against horizontal boxplot
        boxPlot[1, 0].boxplot([LeagueStats['against_per90_a'], LeagueStats['against_per90_h']], vert=False, tick_labels=['Away','Home'], patch_artist=True)
        boxPlot[1, 0].set_title(f'{league} - {year}: Goals Concieded (Home vs Away)')
        boxPlot[1, 0].set_xlabel('Goals Against')

        # Plot xG For horizontal boxplot
        boxPlot[1, 1].boxplot([LeagueStats['xG_per90_a'], LeagueStats['xG_per90_h']], vert=False, tick_labels=['Away','Home'], patch_artist=True)
        boxPlot[1, 1].set_title(f'{league} - {year}: xG - Expected Goals (Home vs Away)')
        boxPlot[1, 1].set_xlabel('xG For')

        # Plot xG Against horizontal boxplot
        boxPlot[2, 0].boxplot([LeagueStats['xGa_per90_a'], LeagueStats['xGa_per90_h']], vert=False, tick_labels=['Away','Home'], patch_artist=True)
        boxPlot[2, 0].set_title(f'{league} - {year}: xGA - Expected Goals Against (Home vs Away)')
        boxPlot[2, 0].set_xlabel('xG Against')

        # Hide the unused subplot
        boxPlot[2, 1].axis('off')
        pvalues_text = (
            f'[Graph 1] Points p-value: {league_points_pvalue:.6f}\n'
            f'[Graph 2] Goals For p-value: {league_goals_for_pvalue:.6f}\n'
            f'[Graph 3] Goals Against p-value: {league_goals_against_pvalue:.6f}\n'
            f'[Graph 4] xG p-value: {league_xG_for_pvalue:.6f}\n'
            f'[Graph 5] xGA p-value: {league_xG_against_pvalue:.6f}'
        )
        boxPlot[2,1].text(0.5, 0.5, pvalues_text, fontsize=12,ha = "center", va= 'center')


        # Save the figure as an image file in the pvalue folder
        folder_path = os.path.join(f'graphs/boxplots/{league}')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Save as PNG file
        file_path = os.path.join(folder_path, f"{league}_{year}_boxplots.png")
        plt.tight_layout()
        plt.savefig(file_path)
        print(f"Horizontal Boxplots for {league} - {year}/{(int(year) + 1)} saved to {file_path}")
        
        # Close the plot to free up memory
        plt.close(fig)

if __name__ == '__main__':
    year = sys.argv[1]
    main(year)
