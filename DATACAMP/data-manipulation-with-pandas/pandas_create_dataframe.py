"""
List of dictionaries
You recently got some new avocado data from 2019 that you'd like to put in a DataFrame
using the list of dictionaries method. Remember that with this method, you go through the data row by row.

date	small_sold	large_sold
"2019-11-03"	10376832	7835071
"2019-11-10"	10717154	8561348
pandas as pd is imported.
"""

import pandas as pd

# Create a list of dictionaries with new data
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)

# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17", "2019-12-01"],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)