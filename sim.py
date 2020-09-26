import pandas as pd
import numpy as np
import random as rnd

gdf = pd.read_csv('updated.csv')
games = pd.read_csv('games.csv')

team1wins = []
team2wins = []
winner = []
for i in range(len(games)):
    team1 = games['team1'][i]
    team2 = games['team2'][i]
    team1df = gdf[gdf.team == team1]
    team2df = gdf[gdf.team == team2]
    team1meanruns = team1df.runs_scored.mean()
    team1sdruns = team1df.runs_scored.std()
    team1oppruns = team1df.runs_allowed.mean()
    team1oppsd = team1df.runs_allowed.std()
    team2meanruns = team2df.runs_scored.mean()
    team2sdruns = team2df.runs_scored.std()
    team2oppruns = team2df.runs_allowed.mean()
    team2oppsd = team2df.runs_allowed.std()

    def gameSim():
        Team1Score = (rnd.gauss(team1meanruns, team1sdruns) +
                      rnd.gauss(team2oppruns, team2oppsd))/2
        Team2score = (rnd.gauss(team2meanruns, team2sdruns) +
                      rnd.gauss(team1oppruns, team2sdruns))/2
        if int(round(Team1Score)) > int(round(Team2score)):
            return 1
        elif int(round(Team1Score)) < int(round(Team2score)):
            return -1
        else:
            return 0

    def gamesSim(ns):
        team1win = 0
        team2win = 0
        tie = 0
        for i in range(ns):
            gm = gameSim()
            if gm == 1:
                team1win += 1
            elif gm == -1:
                team2win += 1
            else:
                tie += 1
        if team1win > team2win:
            winner.append(team1)
        else:
            winner.append(team2)
        team1wins.append(team1win)
        team2wins.append(team2win)
    gamesSim(100000)
games['winners'] = winner
games['team1wins'] = team1wins
games['team2wins'] = team2wins
print(games)
