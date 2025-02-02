import sys
import os
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt

def main(year):

    LEAGUELIST = ['Bundesliga','EPL','La_Liga','Ligue_1','Serie_A']

    for league in LEAGUELIST:
        # Load data into a DataFrame
        LeagueStats = pd.read_csv(f"data/{league}_{year}/pvalue/{league}_{year}_with_pvalues.csv")

        # Calculate p-values
        league_points_pvalue = stats.ttest_ind(LeagueStats['points_h'], LeagueStats['points_a']).pvalue
        league_goals_for_pvalue = stats.ttest_ind(LeagueStats['goals_per90_h'], LeagueStats['goals_per90_a']).pvalue
        league_goals_against_pvalue = stats.ttest_ind(LeagueStats['against_per90_h'], LeagueStats['against_per90_a']).pvalue
        league_xG_for_pvalue = stats.ttest_ind(LeagueStats['xG_per90_h'], LeagueStats['xG_per90_a']).pvalue
        league_xG_against_pvalue = stats.ttest_ind(LeagueStats['xGa_per90_h'], LeagueStats['xGa_per90_a']).pvalue

        # Prepare the figure
        fig, scatterPlot = plt.subplots(3, 2, figsize=(14, 14))
        scatterPlot = scatterPlot.flatten() 

        # Scatter plot for Points
        min_val, max_val = (min(LeagueStats['points_h'].min(), LeagueStats['points_a'].min()),
                            max(LeagueStats['points_h'].max(), LeagueStats['points_a'].max()))
        scatterPlot[0].scatter(LeagueStats['points_h'], LeagueStats['points_a'], alpha=0.7, color='blue')
        scatterPlot[0].plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', linewidth=1.5, label='y=x')
        for metric, team in LeagueStats.iterrows():
            scatterPlot[0].annotate(team['team_title'], (team['points_h'], team['points_a']), textcoords="offset points", xytext=(5, 5), ha='left', fontsize=5)
        scatterPlot[0].set_title(f'{league} - {year}: Points (Home vs Away)')
        scatterPlot[0].set_xlabel('Home')
        scatterPlot[0].set_ylabel('Away')

        # Scatter plot for Goals For
        min_val, max_val = (min(LeagueStats['goals_per90_h'].min(), LeagueStats['goals_per90_a'].min()),
                            max(LeagueStats['goals_per90_h'].max(), LeagueStats['goals_per90_a'].max()))
        scatterPlot[1].scatter(LeagueStats['goals_per90_h'], LeagueStats['goals_per90_a'], alpha=0.7, color='green')
        scatterPlot[1].plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', linewidth=1.5, label='y=x')
        for metric, team in LeagueStats.iterrows():
            scatterPlot[1].annotate(team['team_title'], (team['goals_per90_h'], team['goals_per90_a']), textcoords="offset points", xytext=(5, 5), ha='left', fontsize=5)
        scatterPlot[1].set_title(f'{league} - {year}: Goals Scored (Home vs Away)')
        scatterPlot[1].set_xlabel('Home')
        scatterPlot[1].set_ylabel('Away')

        # Scatter plot for Goals Against
        min_val, max_val = (min(LeagueStats['against_per90_h'].min(), LeagueStats['against_per90_a'].min()),
                            max(LeagueStats['against_per90_h'].max(), LeagueStats['against_per90_a'].max()))
        scatterPlot[2].scatter(LeagueStats['against_per90_h'], LeagueStats['against_per90_a'], alpha=0.7, color='purple')
        scatterPlot[2].plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', linewidth=1.5, label='y=x')
        for metric, team in LeagueStats.iterrows():
            scatterPlot[2].annotate(team['team_title'], (team['against_per90_h'], team['against_per90_a']), textcoords="offset points", xytext=(5, 5), ha='left', fontsize=5)
        scatterPlot[2].set_title(f'{league} - {year}: Goals Conceded (Home vs Away)')
        scatterPlot[2].set_xlabel('Home')
        scatterPlot[2].set_ylabel('Away')

        # Scatter plot for xG
        min_val, max_val = (min(LeagueStats['xG_per90_h'].min(), LeagueStats['xG_per90_a'].min()),
                            max(LeagueStats['xG_per90_h'].max(), LeagueStats['xG_per90_a'].max()))
        scatterPlot[3].scatter(LeagueStats['xG_per90_h'], LeagueStats['xG_per90_a'], alpha=0.7, color='orange')
        scatterPlot[3].plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', linewidth=1.5, label='y=x')
        for metric, team in LeagueStats.iterrows():
            scatterPlot[3].annotate(team['team_title'], (team['xG_per90_h'], team['xG_per90_a']), textcoords="offset points", xytext=(5, 5), ha='left', fontsize=5)
        scatterPlot[3].set_title(f'{league} - {year}: xG - Expected Goals (Home vs Away)')
        scatterPlot[3].set_xlabel('Home')
        scatterPlot[3].set_ylabel('Away')

        # Scatter plot for xGA
        min_val, max_val = (min(LeagueStats['xGa_per90_h'].min(), LeagueStats['xGa_per90_a'].min()),
                            max(LeagueStats['xGa_per90_h'].max(), LeagueStats['xGa_per90_a'].max()))
        scatterPlot[4].scatter(LeagueStats['xGa_per90_h'], LeagueStats['xGa_per90_a'], alpha=0.7, color='brown')
        scatterPlot[4].plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', linewidth=1.5, label='y=x')
        for metric, team in LeagueStats.iterrows():
            scatterPlot[4].annotate(team['team_title'], (team['xGa_per90_h'], team['xGa_per90_a']), textcoords="offset points", xytext=(5, 5), ha='left', fontsize=5)
        scatterPlot[4].set_title(f'{league} - {year}: xGA - Expected Goals Against (Home vs Away)')
        scatterPlot[4].set_xlabel('Home')
        scatterPlot[4].set_ylabel('Away')

        # Hide the unused subplot
        scatterPlot[5].axis('off')
        pvalues_text = (
            f'[Graph 1] Points p-value: {league_points_pvalue:.6f}\n'
            f'[Graph 2] Goals For p-value: {league_goals_for_pvalue:.6f}\n'
            f'[Graph 3] Goals Against p-value: {league_goals_against_pvalue:.6f}\n'
            f'[Graph 4] xG p-value: {league_xG_for_pvalue:.6f}\n'
            f'[Graph 5] xGA p-value: {league_xG_against_pvalue:.6f}'
        )
        scatterPlot[5].text(0.5, 0.5, pvalues_text, fontsize=12,ha = "center", va= 'center')

        # Save the figure
        folder_path = os.path.join(f'graphs/scatterplots/{league}')
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, f"{league}_{year}_scatterplots.png")
        plt.tight_layout()
        plt.savefig(file_path)
        print(f"Scatter plots for {league} - {year}/{(int(year) + 1)} saved to {file_path}")

        plt.close(fig)

if __name__ == '__main__':
    year = sys.argv[1]
    main(year)
