import pandas as pd
from loding_data import df


df.head()

print("total number of null vlaues form the data set --------", df.isnull().sum().sum())
print(df.isnull().sum())

print(df)