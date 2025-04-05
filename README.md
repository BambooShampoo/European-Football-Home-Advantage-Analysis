# Statistical-Analysis-of-Home-Advantage-in-European-Football-2014-2024-
```bash
repository
├── data
│   ├── 2020
│   │   ├── Bundesliga-2020.csv
│   │   ├── EPL-2020.csv
│   │   ├── La_Liga-2020.csv
│   │   ├── ...
│   ├── 2023
│   │   ├── Bundesliga-2023.csv
│   │   ├── EPL-2023.csv
│   │   ├── La_Liga-2023.csv
│   │   ├── ...
│   ├── Bundesliga_2020
│   │   ├── pvalue
│   │   │   ├── Bundesliga_2020_with_pvalue.csv
│   │   ├── Arminia_Bielefeld_Matches_2020.csv
│   │   ├── Augsburg_Matches_2020.csv
│   │   ├── ...
│   ├── Bundesliga_2023
│   │   ├── pvalue
│   │   │   ├── Bundesliga_2023_with_pvalue.csv
│   │   ├── Augsburg_Matches_2023.csv
│   │   ├── Bayer_Leverkusen_Matches_2023.csv
│   │   ├── ...
│   ├── EPL_2020
│   │   ├── pvalue
│   │   │   ├── EPL_2020_with_pvalues.csv
│   │   ├── Arsenal_Matches_2020.csv
│   │   ├── Aston_Villa_Matches_2020.csv
│   │   ├── ...
│   ├── ...
├── graphs
│   ├── scatterplots
│   │   ├── Bundesliga
│   │   │   ├── Bundesliga_2020_scatterplots.png
│   │   │   ├── ...
│   │   ├── EPL
│   │   │   ├── EPL_2020_scatterplots.png
│   │   │   ├── ...
│   │   ├── ...
├── analyseData.py
├── cleanData.py
├── dataBoxplot.py
├── dataHistogram.py
├── gatherData.py
├── leagueDataBoxPlot.py
├── leagueDataHistogram.py
├── leagueDataScatter.py
```

## Libraries required

understatapi 

pandas

numpy

scipy

matplotlib

If any of these librarys are not yet installed:
```bash
pip install understatapi pandas numpy scipy matplotlib
```

## Getting Started with Initial data
Please proceed in the following order

### i)`gatherData.py`
Gathers data from understatapi to reformat and prep for `cleanData.py`, exports as `<league>-<year>.csv` in `data/<year>`
to run, enter in terminal:
```bash
python3 gatherData.py <year>
```

### ii)`cleanData.py`
Uses data from `gatherData.py` as well as match data to create annual match data(match id,side,result,goals_for,goals_against,xG_for,xG_against) for each team and exports it as a csv file in `data/<league>_<year>/` nammed `<team>_<year>.csv` in every league.
to run, enter in terminal:
```bash
python3 cleanData.py <year>
```
Both This program and ` gatherData.py` will take a bit to gather so we already included the nessesary data for 2020 and 2023 as sample data so you can just start from `analyzeData.py`

### iii)`analyzeData.py`
Conducts t-test across every metric from the `cleanData.py` export for every team in every league, exports all the pvalues as well as the home vs away value for each metric in a csv, sorted by total points. Exports as `<league>_<year>_with_pvalues.csv` in `/data/<league>__<year>/pvalue/`
to run, enter in terminal:
```bash
python3 analyzeData.py <year>
```

## Visualising initial Data

### League Data
Creates a graph for each p-value created from `analyzeData.py` and places every team in comparison to each other across the league.
All of these programs export graphs of different metrics for across the league for the top 5 leagues in a specified year.
### i)`leagueDataScatter.py`
to run, enter in terminal:
```bash
python3 leagueDataScatter.py <year>
```

### ii)`leagueDataBoxPlot.py`
to run, enter in terminal:
```bash
python3 leagueDataBoxPlot.py <year>
```

### iii)`leagueDataHistogram.py`
to run, enter in terminal:
```bash
python3 leagueDataHistogram.py <year>
```

### Team Data
Creates a graph for each p-value created from `analyzeData.py` for each team.
All of these programs export graphs of different metrics for each team in the specified league/year.
the list of leagues that can be run are "EPL", "La_Liga", "Bundesliga", "Ligue_1", and "Serie_A" 
### i)`dataBoxplot.py`
to run, enter in terminal:
```bash
python3 leagueDataScatter.py <league> <year>
```

### ii)`dataBoxplot.py`
to run, enter in terminal:
```bash
python3 dataBoxplot.py <league> <year>
```

## Understanding xG and xGA for Non-Football Fans
In football (soccer), two important metrics are Expected Goals (xG) and Expected Goals Against (xGA).

- xG (Expected Goals): This measures the quality of chances a team creates. It calculates how many goals a team should have scored based on the difficulty of their shots. A higher xG means a team is generating better chances.
- xGA (Expected Goals Against): This is the opposite—how many goals a team should have conceded based on the quality of chances the opponent created. A lower xGA means a team is defending well and preventing quality chances.

## What Should You Look At in the Graphs?
Each graph compares Home vs. Away performance for various metrics:

- Points (Graph 1)
- Goals Scored (Graph 2)
- Goals Conceded (Graph 3)
- xG - Expected Goals (Graph 4)
- xGA - Expected Goals Against (Graph 5)

### What the graph shows
- The diagonal red dashed line represents a perfectly balanced team, performing the same at home and away.
- Dots above the line mean the team performs better away in that category.
- Dots below the line mean the team is stronger at home in that category.
- If dots are widely spread from the diagonal, it suggests a big difference in home vs. away performance for that team.

## Findings:
For each league I gathered data from, the home side generates higher xG (expected goals), scores more goals, earned more points on average, 
whereas the away side concede more chances and concede more goals. Each with P-values below 0.05, indicating a convincing different between data values home vs away. 

![image](https://github.com/user-attachments/assets/2a64fb63-13a3-4a54-a7ce-46b7b71ff56a)

However, during the the 2019/2020 season, there was no apparent advantage for any metric.
A giant factor for this is COVID-19, forcing the leagues to play behind closed door, it is quite
apparent that the crowd has influence on games.

### During the COVID-19 lockdown
![image](https://github.com/user-attachments/assets/37cd5e45-dfcd-4e5d-bf55-889ea295a227)

## Comparing 2020 vs. 2023, we can see a shift in home vs. away advantage:

- In 2020, the p-values for all metrics were very high (above 0.2, some close to 1), meaning there was no significant statistical difference between home and away performances.
  - This can be explained by the COVID-19 lockdown, where games were forced to be played behind closed doors.
    
- In 2023, the p-values are much lower (all below 0.05), indicating a significant change in home vs. away dynamics.
  - With fans back in the stadium, they provide a proper push for their team while potentially intimidating the opposing team.

