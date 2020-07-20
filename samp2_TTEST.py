#Two-sample T-test With Python
#The Independent Samples t Test or 2-sample t-test compares the means of two independent groups in order 
#to determine whether there is statistical diff or not
#This test is also known as: Independent t Test

import numpy as np
import pandas as pd
import scipy.stats as stats
import math

np.random.seed(12)

#mu-35 it means all my ages that are getting randomly selected will have a mean of 35,and 60 is my sample size
classA_height=stats.poisson.rvs(mu=30,size=60)
ClassB_height=stats.poisson.rvs(mu=33,size=60)

ClassA_height.mean()
classB_height.mean()

#a-1st sample
#b-sec sample
#equal_var=bool, optional
#If True (default), perform a standard independent 2 sample test that assumes equal population variances 
#If False, perform Welch’s t-test, which does not assume equal population variance 
t_test,p_value=stats.ttest_ind(a=classA_height,b=ClassB_height,equal_var=False)

p_value
if p_value < 0.05:    # alpha value is 0.05 or 5%
    print(" we are rejecting null hypothesis")
else:
    print("we are accepting null hypothesis")
    
 #we are accepting alt.hypo it means there is a statistical difference or we can say
 #mean of 1st sample doesnt equal to 2nd sample

 
 