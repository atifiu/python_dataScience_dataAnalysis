import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
student_data = pd.read_csv('datasets/student-alcohol-consumption.csv')

#student_data = student_data.set_index(['location'])
print(student_data.head())


# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3",
            data=student_data,
            kind="scatter",
            col="schoolsup",
            col_order=["yes", "no"],
            row = 'famsup',
            row_order = ['yes', 'no'])

# Show plot
plt.show()