import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns



#simulate a normally dist population
s=np.random.normal(size=1000)
sns.distplot(s)



#Take a sample
s_sample=np.random.choice(s,size=10,replace=False)
s_sample

np.mean(s_sample)


#Suppose I Want 100 samples of size 10
#more samples we take,more likely that sampling distribution of means will be normally distributed
sample_means=[]
for i in range(100):
    sample=np.random.choice(s,size=10,replace=False)
    sample_means.append(np.mean(sample))
    
sample_means   

sns.distplot(sample_means) 






#Create a skewness population,or a highly skewed distribution
#salary across a larger population
from scipy.stats import skewnorm
x=skewnorm.rvs(6,size=10000)
sns.distplot(x)

#Take a sample
x_sample=np.random.choice(x,size=10,replace=False)
x_sample

np.mean(x_sample)


#Suppose I Want 1000 samples of size 10
#more samples we take,more likely that sampling distribution of means will be normally distributed
sample_means=[]
for i in range(1000):
    sample=np.random.choice(x,size=10,replace=False)
    sample_means.append(np.mean(sample))
    
sample_means   #Suppose I Want 1000 samples of size 10

sns.distplot(sample_means) 









#create a multimodal population
a=np.random.normal(size=1000)
b=np.random.normal(loc=4.0,size=1000)
m=np.concatenate((a,b))
sns.distplot(m)

#Suppose I Want 1000 samples of size 10
sample_means=[]
for i in range(1000):
    sample=np.random.choice(m,size=10,replace=False)
    sample_means.append(np.mean(sample))
    
sample_means   

sns.distplot(sample_means) 