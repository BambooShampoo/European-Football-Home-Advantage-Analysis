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
pip install <library>
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
