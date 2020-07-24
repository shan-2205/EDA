from scipy.stats import binom
import seaborn as sns





#k-no of success, and n=total number of trials
#Question solution
from scipy.stats import binom
s=binom.pmf(k=3,n=5,p=0.75)
s




sum=0
for i in range(3,6):
    from scipy.stats import binom
    s=binom.pmf(k=i,n=5,p=0.75)
    sum=sum+s
    print(s)
sum











