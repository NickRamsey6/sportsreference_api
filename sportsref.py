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


scheds_list = []
for team in Teams():
    sched = team.schedule.dataframe

    sched['home'] = sched.apply(lambda row: home_team(row), axis=1)
    sched['road'] = sched.apply(lambda row: road_team(row), axis=1)

    scheds_list.append(sched)
final = pd.concat(scheds_list)

final2 = final.drop_duplicates(subset=['boxscore_index'])

final.to_csv('duped.csv', index=False)
final2.to_csv('deduped.csv', index=False)


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
