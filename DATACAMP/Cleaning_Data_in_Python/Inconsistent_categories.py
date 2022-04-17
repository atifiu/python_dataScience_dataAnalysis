"""
Inconsistent categories
In this exercise, you'll be revisiting the airlines DataFrame from the previous lesson.

As a reminder, the DataFrame contains flight metadata such as the airline, the destination,
waiting times as well as answers to key questions regarding cleanliness, safety,
and satisfaction on the San Francisco Airport.

In this exercise, you will examine two categorical columns from this DataFrame,
dest_region and dest_size respectively, assess how
to address them and make sure that they are cleaned and ready for analysis.
The pandas package has been imported as pd,
and the airlines DataFrame is in your environment.
"""

import pandas as pd
import numpy as np

airlines = pd.read_csv('datasets/airlines_final.csv')

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip()

# Verify changes have been effected
print(airlines['dest_size'].unique())
print(airlines['dest_region'].unique())

"""
Remapping categories
To better understand survey respondents from airlines, you want to find out if there is a relationship between certain responses and the day of the week and wait time at the gate.

The airlines DataFrame contains the day and wait_min columns, which are categorical and numerical respectively. The day column contains the exact day a flight took place, and wait_min contains the amount of minutes it took travelers to wait at the gate. To make your analysis easier, you want to create two new categorical variables:

wait_type: 'short' for 0-60 min, 'medium' for 60-180 and long for 180+
day_week: 'weekday' if day is in the weekday, 'weekend' if day is in the weekend.
The pandas and numpy packages have been imported as pd and np. Let's create some new categorical data!
"""

# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, labels = label_names)

# Create mappings and replace
mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday',
            'Thursday': 'weekday', 'Friday': 'weekday',
            'Saturday': 'weekend', 'Sunday': 'weekend'}
assert any(airlines['day'] == 'Sunday')


airlines['day_week'] = airlines['day'].replace(mappings)

assert any(airlines['day_week'].isin(['Sunday', 'weekend']))
assert any(airlines['day_week'] == 'weekend')
