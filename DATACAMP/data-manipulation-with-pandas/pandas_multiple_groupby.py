"""
Multiple grouped summaries
Earlier in this chapter, you saw that the .agg() method is useful to compute multiple statistics on multiple variables. It also works with grouped data. NumPy, which is imported as np, has many different summary statistics functions, including: np.min, np.max, np.mean, and np.median.

sales is available and pandas is imported as pd
"""

import pandas as pd

sales = pd.read_csv('datasets/sales_subset.csv')

# Import numpy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')["weekly_sales"].agg([np.min, np.max,np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')["unemployment", "fuel_price_usd_per_l"].agg([np.min, np.max,np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)