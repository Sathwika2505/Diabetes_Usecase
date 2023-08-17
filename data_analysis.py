import pandas as pd
from loding_data import output, column_names


df = pd.DataFrame(output, columns = column_names )
df.head()

print("total number of null vlaues form the data set --------", df.isnull().sum().sum())
print(df.isnull().sum())

print(df)