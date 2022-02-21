"""
Slicing time series
Slicing is particularly useful for time series since it's a common thing to want to filter
for data within a date range. Add the date column to the index, then use .loc[] to perform the subsetting.
The important thing to remember is to keep your dates in ISO 8601 format, that is, "yyyy-mm-dd"
for year-month-day, "yyyy-mm" for year-month, and "yyyy" for year.

Recall from Chapter 1 that you can combine multiple Boolean conditions using
logical operators, such as &. To do so in one line of code, you'll need
to add parentheses () around each condition.

pandas is loaded as pd and temperatures, with no index, is available
"""

import pandas as pd

temperatures = pd.read_csv('datasets/temperatures.csv')

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011

temperatures_bool = temperatures[(temperatures["date"] >= '2010-01-01') & (temperatures["date"] <= '2011-12-31')]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])
