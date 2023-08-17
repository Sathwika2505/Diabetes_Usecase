import pandas as pd
import numpy as np
from data_analysis import df

copy_df = df
new_df = copy_df.dropna()
new_df

copy_df.fillna(0, inplace = True)

new_df.drop_duplicates(inplace = True)
print(new_df.duplicated())

#new_df['age'] = np.floor(new_df['age'])
new_df['age'] = new_df['age'].astype('int')
new_df['age']

df = new_df

print(df)