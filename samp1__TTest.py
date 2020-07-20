#consider the age of students in a college and in Class A


import numpy as np
import pandas as pd
import scipy.stats as stats
import math
np.random.seed(6)
school_ages=stats.poisson.rvs(mu=35,size=1500)
#size-total values we want
#mu=mean and loc is left most value and its poisson distribution(poisson rvs)
classA_ages=stats.poisson.rvs(mu=30,size=60)
classA_ages.mean()


classA_ages.mean()

ttest,p_value=stats.ttest_1samp(a=classA_ages,popmean=school_ages.mean())

p_value

school_ages.mean()

if p_value < 0.05:    # alpha value is 0.05 or 5%
    print(" we are rejecting null hypothesis")
else:
    print("we are accepting null hypothesis")
    
    
 #as p_value is very low,it means we are rejecting null hypothesis,ie we are accpeting alt hypo
 #it means sampling mean doesnt equal to population mean or there is a difference between sampling mean
 # of age and pop. mean of age