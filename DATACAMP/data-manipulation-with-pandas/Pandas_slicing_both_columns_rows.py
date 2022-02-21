"""
Slicing in both directions
You've seen slicing DataFrames by rows and by columns, but since DataFrames are two-dimensional objects,
it is often natural to slice both dimensions at once. That is, by passing two arguments to .loc[],
you can subset by rows and columns in one go.

pandas is loaded as pd. temperatures_srt is indexed by country and city, has a sorted index,
and is available.
"""

import pandas as pd

temperatures = pd.read_csv('datasets/temperatures.csv')

temperatures_ind = temperatures.set_index(["country", "city"])

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad')])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,'date':'avg_temp_c'])

# Subset in both directions at once
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad'),'date':'avg_temp_c'])

print(temperatures.shape)
help(temperatures.sort_index)

