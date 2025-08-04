import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
mobiles=pd.read_csv('mobiles1.csv')
print(mobiles.info)
print(mobiles.dtypes)
print(mobiles.columns.duplicated())
sns.histplot(data=mobiles,x='price',bins=20)
plt.show()
sns.barplot(data=mobiles,x='rating',y='price')
plt.show()
sns.boxplot(data=mobiles,x='price')
plt.show()
print(mobiles['price'].mean())
print(mobiles['price'].mode()[0])
print(mobiles['price'].skew())
print(mobiles.isnull().sum())
print(mobiles.describe())
mobiles.dropna(inplace=True)
print(mobiles.isnull().sum())
correlationvals=mobiles.corr(numeric_only=True)
print(correlationvals)
print(mobiles.kurtosis(numeric_only=True))
mobiles.drop_duplicates(inplace=True)
plt.scatter(data=mobiles,x='rating',y='price')
plt.show()
#make a html file
from ydata_profiling import ProfileReport
df = pd.read_csv("mobiles1.csv")
profile = ProfileReport(df, title="Mobile Dataset EDA Report", explorative=True)
profile.to_file("mobile_eda_report.html")
