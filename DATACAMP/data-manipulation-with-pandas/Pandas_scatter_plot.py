"""
Avocado supply and demand
Scatter plots are ideal for visualizing relationships between numerical variables. In this exercise, you'll compare the number of avocados sold to average price and see if they're at all related. If they're related, you may be able to use one number to predict the other.

matplotlib.pyplot has been imported as plt and pandas has been imported as pd.
"""
import pandas as pd
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt



avocados = pd.read_pickle('datasets/avoplotto.pkl')

#help(pd.DataFrame.plot)

# Scatter plot of nb_sold vs avg_price with title
print(avocados.head())
help(pd.DataFrame.plot)
avocados.plot(x = "nb_sold", y = "avg_price", title = "Number of avocados sold vs. average price", kind = "scatter")

# Show the plot
plt.show()

"""
Price of conventional vs. organic avocados
Creating multiple plots for different subsets of data allows you to compare groups. In this exercise, you'll create multiple histograms to compare the prices of conventional and organic avocados.

matplotlib.pyplot has been imported as plt and pandas has been imported as pd"""

# Histogram of conventional avg_price
avocados[avocados["type"] == "conventional"]["avg_price"].hist()

# Histogram of organic avg_price
avocados[avocados["type"] == "organic"]["avg_price"].hist()

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()


# Modify histogram transparency to 0.5
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha = 0.5, bins = 20)

# Modify histogram transparency to 0.5
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha = 0.5, bins = 20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()