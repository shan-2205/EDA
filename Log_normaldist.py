#Create a skewness population,or a highly skewed distribution
#salary across a larger population
from scipy.stats import skewnorm
x=skewnorm.rvs(6,size=10000)
sns.distplot(x)