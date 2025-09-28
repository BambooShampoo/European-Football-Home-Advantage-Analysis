import subprocess
import sys

def run_pipeline(year: str):
    scripts = [
        "gatherData.py",
        "cleanData.py",
        "analyseData.py",
        "leagueDataScatter.py",
        "leagueDataBoxPlot.py",
        "leagueDataHistogram.py",
    ]

    for script in scripts:
        print(f"\n>>> Running {script} {year} ...")
        subprocess.run(["python3", script, year], check=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 run_pipeline.py <year>")
        sys.exit(1)

    year = sys.argv[1]
    run_pipeline(year)
