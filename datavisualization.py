import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import df
import numpy as np

copy2_df = df
sns.countplot(data = copy2_df, x = "smoking_history")
plt.show() 

sns.countplot(data = copy2_df, x = "gender")
plt.show() 

sns.countplot(data = copy2_df, x = "blood_glucose_level")
plt.show() 

fig, ax = plt.subplots()
sns.scatterplot(data = copy2_df, ax=ax, x = 'age', y = 'bmi')
ax.set_ylim(1, 100)
ax.set_xlim(1, 85)
plt.show()

fig, ax = plt.subplots()
sns.barplot(data = copy2_df, x = 'HbA1c_level', y = 'age')
y_ticks = np.arange(0, 81, 10)
ax.set_yticks(y_ticks)
ax.set_ylim(1, 80)

df = copy2_df
print(df)