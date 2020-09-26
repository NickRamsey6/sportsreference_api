from sportsreference.mlb.schedule import Schedule
import pandas as pd
import numpy as np


sea_schedule = Schedule('SEA')
sea_df = sea_schedule.dataframe

print(sea_df.iloc[1].shift())
