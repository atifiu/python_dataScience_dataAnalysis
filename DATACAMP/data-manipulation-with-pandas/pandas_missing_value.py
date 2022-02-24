"""
Finding missing values
Missing values are everywhere, and you don't want them interfering with your work. Some functions ignore missing data by default, but that's not always the behavior you might want. Some functions can't handle missing values at all, so these values need to be taken care of before you can use them. If you don't know where your missing values are, or if they exist, you could make mistakes in your analysis. In this exercise, you'll determine if there are missing values in the dataset, and if so, how many.

pandas has been imported as pd and avocados_2016, a subset of avocados that contains only sales from 2016, is available
"""

import pandas as pd
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt



avocados = pd.read_pickle('datasets/avoplotto.pkl')
#print(avocados.head())
avocados_2016 = avocados.query('date >= "2016-01-01" and date <= "2016-12-31"')
print(avocados_2016.info())
print(avocados_2016["date"].agg(['max', 'min']))

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind = "bar")

# Show plot
plt.show()

"""
Removing missing values
Now that you know there are some missing values in your DataFrame, you have a few options to deal with them. One way is to remove them from the dataset completely. In this exercise, you'll remove missing values by removing all rows that contain missing values.

pandas has been imported as pd and avocados_2016 is available."""

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())

# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
print(avocados_2016.info())

# Create histograms showing the distributions cols_with_missing
#avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()