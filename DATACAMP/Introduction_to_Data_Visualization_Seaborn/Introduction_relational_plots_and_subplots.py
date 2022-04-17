import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')
print(df.head())
#sns.scatterplot(x = 'total_bill', y = 'tip', data = df, hue = 'smoker')


#plt.show()

#sns.relplot(x = 'total_bill', y = 'tip', data = df, kind = 'scatter', col = "smoker", row = "time")

# Change this scatter plot to arrange the plots in rows instead of columns
student_data = pd.read_csv('datasets/student-alcohol-consumption.csv')
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter",
            row="study_time")

# Show plot
plt.show()

plt.show()

