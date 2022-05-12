import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
In this exercise, we'll explore Seaborn's mpg dataset, which contains one row per car model and includes information such as the year the car was made, the number of miles per gallon ("M.P.G.") it achieves, the power of its engine (measured in "horsepower"), and its country of origin.

What is the relationship between the power of a car's engine ("horsepower") and its fuel efficiency ("mpg")? And how does this relationship vary by the number of cylinders ("cylinders") the car has? Let's find out.

Let's continue to use relplot() instead of scatterplot() since it offers more flexibility.
'''
mpg = pd.read_csv('datasets/mpg.csv')
print(mpg.head())

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg",
            data=mpg, kind="scatter",
            size="cylinders",
            hue = 'cylinders')

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x = 'acceleration', y = 'mpg', data = mpg,
style = 'origin', hue = 'origin', kind = 'scatter' )



# Show plot
plt.show()

