'''
merge_ordered is similar to merge except that it will sort the result set
and default join is outer

In this exercise, you want to analyze stock returns from the S&P 500.
You believe there may be a relationship between
the returns of the S&P 500 and the GDP of the US. Merge the different
datasets together to compute the correlation.

Two tables have been provided for you, named sp500, and gdp.
 As always, pandas has been imported for you as pd.
'''

import pandas as pd
sp500 = pd.read_csv('./dataset/S&P500.csv')
gdp = pd.read_csv('./dataset/WorldBank_GDP.csv')
print(sp500)
# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='Year', right_on='Date',
                             how='left',   fill_method='ffill')

# Print gdp_sp500
print(gdp_sp500)

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['GDP', 'Returns']]

# Print gdp_returns correlation
print(gdp_returns.corr())
