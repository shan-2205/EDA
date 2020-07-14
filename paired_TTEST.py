#Paired T-test With Python
#When you want to check how different samples from the same group are, you can go for a paired T-test
import numpy as np
import pandas as pd
import scipy.stats as stats


weight1=[25,30,28,35,28,34,26,29,30,26,28,32,31,30,45]

#suppose after some years wts of students changes
weight2=weight1+stats.norm.rvs(scale=5,loc=-1.25,size=15)

print(weight1)
print(weight2)

weight_df=pd.DataFrame({"weight_10":np.array(weight1),
                         "weight_20":np.array(weight2),
                       "weight_change":np.array(weight2)-np.array(weight1)})

weight_df

_,p_value=stats.ttest_rel(a=weight1,b=weight2)

print(p_value)


if p_value < 0.05:    # alpha value is 0.05 or 5%
    print(" we are rejecting null hypothesis")
else:
    print("we are accepting null hypothesis")
#we are accepting null hypothesis means there is no statistical difference between both sample of same grp