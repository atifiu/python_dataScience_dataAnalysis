'''
merge has validate arguments if set to one_to_one then it will validate if one_to_one relationship exists or not
otherwise it will throw error

Likewise Concat has verify_integrity which has default value of False but if set to True it will ensure that index
on cancatenate dataframe has not duplicate index value

# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on = 'tid')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)
'''

import pandas as pd
