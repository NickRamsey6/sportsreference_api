import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import Ridge

# load the data
df = pd.read_csv('rr.csv', skiprows=1, names=[
                 'date', 'visitor', 'visitor_runs', 'home', 'home_runs'])

# make the date column into a date format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

df['run_difference'] = df['home_runs'] - df['visitor_runs']

# create new variables to show home team win or loss result
df['home_win'] = np.where(df['run_difference'] > 0, 1, 0)
df['home_loss'] = np.where(df['run_difference'] < 0, 1, 0)


df_visitor = pd.get_dummies(df['visitor'], dtype=np.int64)
df_home = pd.get_dummies(df['home'], dtype=np.int64)

# subtract home from visitor
df_model = df_home.sub(df_visitor)
df_model['run_difference'] = df['run_difference']

df_train = df_model

lr = Ridge(alpha=0.001)
X = df_train.drop(['run_difference'], axis=1)
y = df_train['run_difference']

lr.fit(X, y)

df_ratings = pd.DataFrame(data={'team': X.columns, 'rating': lr.coef_})
print(df_ratings)
