from sportsreference.mlb.teams import Teams
from sportsreference.mlb.boxscore import Boxscore
from sportsreference.mlb.schedule import Schedule
import pandas as pd

# indexes = []
# for team in Teams():
#     schedule = team.schedule  # Request the current team's schedule

#     for game in schedule:

#         indexes.append(game.boxscore_index)

# # Remove empty tables
# a = [x for x in indexes if "td" not in x]
# # print(len(a))


# # Remove duplicate indexes
# def de_dupe(x):
#     return list(dict.fromkeys(x))


# indexes_dedupped = de_dupe(a)

# # Iterate through list of boxscore indexes
# games = indexes_dedupped
# for game in games:
#     g = Boxscore(game)
#     print(g.home_runs)

def home_team(row):
    if row['location'] == 'Away':
        return row['opponent_abbr']
    return team.abbreviation


def road_team(row):
    if row['location'] == 'Away':
        return team.abbreviation
    return row['opponent_abbr']


def home_team_runs(row):
    if row['location'] == 'Away':
        return row['runs_allowed']
    return row['runs_scored']


def road_team_runs(row):
    if row['location'] == 'Away':
        return row['runs_scored']
    return row['runs_allowed']


def winning_team(row):
    if row['result'] == 'Win':
        return team.abbreviation
    return row['opponent_abbr']


scheds_list = []
for team in Teams('2019'):
    sched = team.schedule.dataframe
    # sched['datetime'] = pd.to_datetime(sched['datetime'], format='%d%mm%Y')

    # sched['datetime'] = sched['datetime'].astype('string')
    # sched['home'] = sched.apply(lambda row: home_team(row), axis=1)
    # sched['road'] = sched.apply(lambda row: road_team(row), axis=1)
    # sched['home_team_runs'] = sched.apply(
    #     lambda row: home_team_runs(row), axis=1)
    # sched['road_team_runs'] = sched.apply(
    #     lambda row: road_team_runs(row), axis=1)
    sched['team'] = team.abbreviation
    # sched['cum_runs_scored'] = sched['runs_scored'].cumsum()
    # sched['cum_runs_allowed'] = sched['runs_allowed'].cumsum()
    # sched['ytd_rd'] = (sched['cum_runs_scored'] -
    #                    sched['cum_runs_allowed'])/sched['game']
    # sched['winning_team'] = sched.apply(lambda row: winning_team(row), axis=1)
    # all_days = pd.date_range(
    #     sched['datetime'].min(), sched['datetime'].max(), freq='D')
    # sched.loc[all_days]

    # FAILED sumif by date
    # sched['league_home_team_runs'] = sched.groupby(
    #     ['datetime'])['home_team_runs'].sum()

    scheds_list.append(sched)
final = pd.concat(scheds_list)

# final.index = pd.DatetimeIndex(final['datetime'])
# final3 = final.reindex(idx, fill_value=0)

# Bring back drop dupes line
# final2 = final.drop_duplicates(subset=['boxscore_index'])
# final2['league_home_team_runs'] = final2.groupby(
#     'datetime')['home_team_runs'].sum()

# BRING BACK CSVs
final.to_csv('2019.csv', index=False)
# final2.to_csv('deduped2.csv', index=False)
# final3.to_csv('dated.csv', index=false)


# sea_schedule = Schedule('SEA')
# sea_df = sea_schedule.dataframe

# locations = sea_df['location']

# Add home team column to schedule dataframe


# def home_team(row):
#     if row['location'] == 'Away':
#         return row['opponent_abbr']
#     return team.name


# sea_df['home'] = sea_df.apply(lambda row: home_team(row), axis=1)

# Add home team column to schedule dataframe


# def road_team(row):
#     if row['location'] == 'Away':
#         return 'SEA'
#     return row['opponent_abbr']


# sea_df['road'] = sea_df.apply(lambda row: road_team(row), axis=1)

# print(sea_df)


# home_runz = []
# away_runz = []
# for game in indexes_dedupped:
#     boxscore = game.boxscore
#     home_runz.append(boxscore.home_runs)

# print(home_runz)

# # cols = ['date', 'visitor', 'vis score', 'home', 'home score']
# # lst = []

# rd = []
# teams = Teams()
# for team in teams:
#     print(team.name)  # Prints the team's name
#     # Prints the team's season batting average
#     print(team.pythagorean_win_loss)
