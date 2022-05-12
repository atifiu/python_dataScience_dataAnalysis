import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Let's continue exploring the responses to a survey sent out to young people. T
he variable "Interested in Math" is True if the person reported being interested or 
very interested in mathematics, and False otherwise. 
What percentage of young people report being interested in math, 
and does this vary based on gender? Let's use a bar plot to find out.

As a reminder, we'll create a bar plot using the catplot() function,
 providing the name of categorical variable to put on the x-axis (x=____), the name of the quantitative variable to summarize on the y-axis (y=____), the pandas DataFrame to use (data=____), and the type of categorical plot (kind="bar").


'''

survey_data = pd.read_csv('datasets/young-people-survey-responses.csv')

#survey_data.loc[survey_data['Mathematics'] >= 4, 'Interested in Math'] = True
#survey_data.loc[survey_data['Mathematics'] < 4, 'Interested in Math'] = False
survey_data['Interested in Math'] = np.where(survey_data['Mathematics'] >= 4, True, False)
print(survey_data[['Mathematics', "Interested in Math"]].head())
#print(survey_data.columns)

# Create a bar plot of interest in math, separated by gender

sns.catplot(x = 'Gender', y = 'Interested in Math', data = survey_data, kind = 'bar')

# Create bar plot of average final grade in each study category

student_data = pd.read_csv('datasets/student-alcohol-consumption.csv')

sns.catplot(x='study_time', y='G3', data=student_data, kind ='bar')

# List of categories from lowest to highest
category_order = ["<2 hours",
                  "2 to 5 hours",
                  "5 to 10 hours",
                  ">10 hours"]

# Rearrange the categories
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar", order = category_order)

plt.show()