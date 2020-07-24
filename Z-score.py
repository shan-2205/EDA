
import pandas as pd
df=pd.read_csv('F:/Statistics/Data/blood_pressure.csv')
df

from sklearn.preprocessing import StandardScaler
scaling=StandardScaler()

#fit_transform-Fit to data, then transform it.
scaling.fit_transform(df[['bp_before','bp_after']])

