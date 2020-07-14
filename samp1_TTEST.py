#One-sample T-test with Python
#The test will tell us whether means of the sample and the population are different


#Suppose I create a population as
ages=[10,30,25,43,18,20,35,50,28,40,55,18,16,55,30,28,14,24,16,17,32,35,26,27,65,18,43,23,21,20,19,70]
len(ages)



import numpy as np
ages_mean=np.mean(ages)
ages_mean



## Lets randomly pick sample from population
sample_size=8
sample_age=np.random.choice(ages,sample_size)
sample_age


#then import library
from scipy.stats import ttest_1samp
#gives 2 values,ttest value and pvalue
#suppose I consider popmean as-30,then my null hypo says thatwhether this value is going to be 30
#which i considered as my pop mean or not 30
#if it is 30,then i can say there is no diff,then I can say my null is true
ttest,p_value=ttest_1samp(sample_age,30)
print(p_value)


if p_value < 0.05:    # alpha value is 0.05 or 5%
    print(" we are rejecting null hypothesis")
else:
    print("we are accepting null hypothesis")
    
#as p value is greater than 0.05 it means we are accepting null hypo
    #ie there is no difference in sampling mean of age and population mean of age