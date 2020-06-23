import pandas as pd
import numpy as np

df = pd.DataFrame([[0, np.nan, 3], [np.nan, 4, 1], [10, np.nan, 30]], index=[4, 5, 6], columns=['A', 'B', 'C'])
df['B'].fillna(value=-1, inplace=True)
print(df)
