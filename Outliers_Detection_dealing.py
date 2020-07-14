import pandas as pd
df=pd.read_csv('mtcars.csv')

df.shape

import seaborn as sns
sns.boxplot(data=df,x=df['hp'])


Q1=df['hp'].quantile(0.25)
Q3=df['hp'].quantile(0.75)
IQR=Q3-Q1
print(Q1)
print(Q3)
print(IQR)
Lower_whisker=Q1-1.5*IQR
Upper_Whisker= Q3+1.5*IQR
print(Lower_whisker, Upper_Whisker)
     #28.75 305.25  
     #Means between thids range,we dont have any outliers
          
df = df[df['hp']< Upper_Whisker]