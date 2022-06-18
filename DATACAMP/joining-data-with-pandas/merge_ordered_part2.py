'''
merge_ordered() caution, multiple columns
When using merge_ordered() to merge on multiple columns, the order is important when you combine it with the forward fill feature. The function sorts the merge on columns in the order provided. In this exercise, we will merge GDP and population data from the World Bank for the Australia and Sweden, reversing the order of the merge on columns. The frequency of the series are different, the GDP values are quarterly, and the population is yearly. Use the forward fill feature to fill in the missing data. Depending on the order provided, the fill forward will use unintended data to fill in the missing values.

The tables gdp and pop have been loaded.
'''

import pandas as pd
gdp = pd.read_csv('./dataset/WorldBank_GDP.csv')
#print(gdp.head(5))
#print(gdp['Country Name'].unique())
gdp = gdp.loc[gdp['Country Name'].isin(['Germany', 'Japan'])]
#print(gdp.head(5))
print(gdp.columns)
pop = pd.read_csv('./dataset/WorldBank_POP.csv')
#print(pop['Country Name'].unique())
pop = pop.loc[pop['Country Name'].isin(['Germany', 'Japan'])]
#print(pop.head(10))
print(pop.columns)

# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp,pop, on = ['Year', 'Country Name'] ,fill_method='ffill')

# Print ctry_date
print(ctry_date)