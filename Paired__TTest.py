
#When you want to check how different samples from the same group are, you can go for a paired T-test

from scipy import stats
import pandas as pd
df=pd.read_csv('F:/Statistics/Data/Blood_pressure.csv')
df
df[['bp_before','bp_after']].describe()


#The hypothesis being test is:
#Null hypothesis (H0): u = 0, which says mean difference between sample 1 and sample 2 is equal to 0.
#Alternative hypothesis (HA): u ≠ 0, which says mean difference between sample 1 and sample 2 is not equal to 0.


t,p_value=stats.ttest_rel(df['bp_before'], df['bp_after'])
p_value
if p_value < 0.05:    # alpha value is 0.05 or 5%
    print(" we are rejecting null hypothesis")
else:
    print("we are accepting null hypothesis")






#INTERPRETATION OF THE RESULTS
#A paired sample t-test was used to analyze the blood pressure before and after the intervention to test 
#if the intervention had a significant affect on the blood pressure. The blood pressure before the intervention 
#was higher (156.45 ± 11.38 units) compared to the blood pressure post intervention (151.35 ± 14.17 units); 
#there was a statistically significant decrease in blood pressure
    #we are rejecting null hypothesis means mean diff will not be 0,it means I have a statistical
    #diff between both samples