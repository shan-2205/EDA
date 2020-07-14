#Two-sample T-test With Python
#The Independent Samples t Test or 2-sample t-test compares the means of two independent groups in order to determine whether there is statistical evidence that the associated population means are significantly different. The Independent Samples t Test is a parametric test. This test is also known as: Independent t Test

import numpy as np
import pandas as pd
import scipy.stats as stats
import math

np.random.seed(12)
classA_height=stats.poisson.rvs(loc=18,mu=30,size=60)
ClassB_ages=stats.poisson.rvs(loc=18,mu=33,size=60)
ClassB_ages.mean()
classA_height.mean()

_,p_value=stats.ttest_ind(a=classA_height,b=ClassB_ages,equal_var=False)

p_value
if p_value < 0.05:    # alpha value is 0.05 or 5%
    print(" we are rejecting null hypothesis")
else:
    print("we are accepting null hypothesis")
    
 #we are accepting alt.hypo it means there is a statistical difee or
 #sampling mean doesnt equal to pop. mean