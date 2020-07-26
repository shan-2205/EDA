#Create a skewness population,or a highly skewed distribution
#salary across a larger population
from scipy.stats import skewnorm
x=skewnorm.rvs(6,size=10000)
sns.distplot(x)


from scipy.stats import expon
import seaborn as sns
data_expon = expon.rvs(scale=1,loc=0,size=1000)


ax = sns.distplot(data_expon,
                  kde=True,
                  bins=100,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Exponential Distribution', ylabel='Frequency')








