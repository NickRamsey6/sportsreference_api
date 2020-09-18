from sportsreference.mlb.teams import Teams

indexes = []
for team in Teams():
    schedule = team.schedule  # Request the current team's schedule

    for game in schedule:

        indexes.append(game.boxscore_index)

# Remove empty tables
a = [x for x in indexes if "td" not in x]
print(len(a))


# Remove duplicate indexes
def de_dupe(x):
    return list(dict.fromkeys(x))


indexes_dedupped = de_dupe(a)
print(len(indexes_dedupped))
