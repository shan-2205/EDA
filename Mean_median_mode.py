import pandas as pd
import numpy as np
import statistics
#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','Tom','Ricky','Vin','Steve','Smith','Jack',
   'Lee','Chanchal','Gasper','Naviya','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print("Mean Values in the Distribution")
print(df.mean())
print('/n')
print("Median Values in the Distribution")
print(df.median())



#To calculate mode,we have to import lib statistics
statistics.mode(df['Name'])


# Calculate the standard deviation
print(df.std())



#Measuring Skewness
#It used to determine whether the data is symmetric or skewed. If the index is between -1 and 1, then 
#the distribution is symmetric. If the index is no more than -1 then it is skewed to the left and if it is at least 1,
#then it is skewed to the right
df.skew()
