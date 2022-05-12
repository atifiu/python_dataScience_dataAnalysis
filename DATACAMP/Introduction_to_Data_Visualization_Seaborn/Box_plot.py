import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Let's continue using the student_data dataset. In an earlier exercise, we explored the relationship between studying and final grade by using a bar plot to compare the average final grade ("G3") among students in different categories of "study_time".

In this exercise, we'll try using a box plot look at this relationship instead. As a reminder, to create a box plot you'll need to use the catplot() function and specify the name of the categorical variable to put on the x-axis (x=____), the name of the quantitative variable to summarize on the y-axis (y=____), the pandas DataFrame to use (data=____), and the type of plot (kind="box").
'''

student_data = pd.read_csv('datasets/student-alcohol-consumption.csv')

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours",
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x = 'study_time', y='G3', data = student_data, order = study_time_order, kind = 'box')

'''
Omitting outliers
Now let's use the student_data dataset to compare the distribution of final grades ("G3") between students who have internet access at home and those who don't. To do this, we'll use the "internet" variable, which is a binary (yes/no) indicator of whether the student has internet access at home.

Since internet may be less accessible in rural areas, we'll add subgroups based on where the student lives. For this, we can use the "location" variable, which is an indicator of whether a student lives in an urban ("Urban") or rural ("Rural") location.

Seaborn has already been imported as sns and matplotlib.pyplot has been imported as plt. As a reminder, you can omit outliers in box plots by setting the sym parameter equal to an empty string ("").
'''

# Create a box plot with subgroups and omit the outliers

sns.catplot(data = student_data, x='internet', y='G3', col='location', sym="", kind = 'box', hue = 'location')

# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])

sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2, join = False)
# Show plot
plt.show()