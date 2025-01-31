import numpy as np
import pandas as pd

filename = '/chicago.csv'

# load data file into a dataframe
df = pd.read_csv(filename)
print(df['Start Time'].head())

# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])
print(df['Start Time'].head())

# extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour
print(df['hour'].head())

# find the most common hour (from 0 to 23)
popular_hour = df['hour'].mode()[0]
print('Most Popular Start Hour:', popular_hour)