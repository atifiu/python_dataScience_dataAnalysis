"""
Changes in sales over time
Line plots are designed to visualize the relationship between two numeric variables, where each data values is connected to the next one. They are especially useful for visualizing the change in a number over time since each time point is naturally connected to the next time point. In this exercise, you'll visualize the change in avocado sales over three years.

pandas has been imported as pd
"""

import pandas as pd
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt



avocados = pd.read_pickle('datasets/avoplotto.pkl')



# Get the total number of avocados sold on each date

nb_sold_by_date = avocados.groupby("date")['nb_sold'].sum()

print(nb_sold_by_date.head())

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind = "line")

# Show the plot
plt.show()