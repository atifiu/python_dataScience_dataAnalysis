import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
In this exercise, we'll return to exploring our dataset that contains the responses to a survey sent out to young people. We might suspect that young people spend a lot of time on the internet, but how much do they report using the internet each day? Let's use a count plot to break down the number of survey responses in each category and then explore whether it changes based on age.

As a reminder, to create a count plot, we'll use the catplot() function and specify the name of the categorical variable to count (x=____), the pandas DataFrame to use (data=____), and the type of plot (kind="count").

Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt
'''
survey_data = pd.read_csv('datasets/young-people-survey-responses.csv')

print(survey_data.columns)
max_age = survey_data['Age'].max()
print("Max age", max_age)
print(survey_data.describe())
survey_data['Age Category'] = 'Less than 21'
survey_data.loc[survey_data['Age'] < 21, 'Age Category'] = 'Less than 21'
survey_data.loc[survey_data['Age'] >= 21, 'Age Category'] = 'More than 21'
print(survey_data.loc[:,['Age', 'Age Category']].sample(10))
#survey_data = survey_data['Age Category'].astype('category')
survey_data = survey_data.astype({"Age Category":'category'})
print(survey_data.info())
#survey_data['Age Category'] = pd.cut(survey_data['Age'] , bins=[0, 21, max_age], labels = ['Less than 21', 'More than 21'])

# Create count plot of internet usage
sns.catplot(x = 'Internet usage', data = survey_data, kind = 'count')

# Change the orientation of the plot
sns.catplot(y="Internet usage", data=survey_data,
            kind="count")

# Separate into column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col = 'Age Category')

# Create a bar plot of interest in math, separated by gender

sns.catplot(x = 'Gender', y = 'Interested in Math', data = survey_data, kind = 'bar')
# Show plot
plt.show()