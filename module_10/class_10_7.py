import pandas as pd
filename = 'chicago.csv'
# load data file into a dataframe
df = pd.read_csv(filename)
# print value counts for each user type
user_types = df['User Type'].value_counts(dropna=False)
print(user_types)