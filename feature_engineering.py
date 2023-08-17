import pandas as pd
import numpy as np
from datavisualization import df
from sklearn import preprocessing

copy3_df = df
label_encoder = preprocessing.LabelEncoder()
copy3_df['smoking_history'] = label_encoder.fit_transform(copy3_df['smoking_history'])

label_df = copy3_df['smoking_history'].unique()
print(label_df)

copy3_df['gender'] = label_encoder.fit_transform(copy3_df['gender'])
lab_df = copy3_df['gender'].unique()
print(lab_df) 

df = copy3_df
print(df)

