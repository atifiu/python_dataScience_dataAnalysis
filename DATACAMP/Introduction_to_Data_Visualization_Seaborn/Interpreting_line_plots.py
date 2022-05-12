import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
In this exercise, we'll continue to explore Seaborn's mpg dataset, which contains one row per car model and includes information such as the year the car was made, its fuel efficiency (measured in "miles per gallon" or "M.P.G"), and its country of origin (USA, Europe, or Japan).

How has the average miles per gallon achieved by these cars changed over time? Let's use line plots to find out!.
'''
mpg = pd.read_csv('datasets/mpg.csv')
print(mpg.head())

# Create line plot
sns.relplot(x = 'model_year', y = 'mpg', data = mpg, kind = 'line')

# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci = "sd")

# Create line plot of model year vs. horsepower
sns.relplot(x="model_year", y="horsepower",
            data=mpg, kind="line", ci = None)

# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower",
            data=mpg, kind="line",
            ci=None, style="origin",
            hue="origin", markers = True, dashes = False)


# Show plot
plt.show()