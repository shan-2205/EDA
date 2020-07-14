from scipy.stats import binom
import seaborn as sns

#n is basically ur highest number in ur array
data_binom = binom.rvs(n=30,p=0.8,size=1000)



#visualising by graph
sns.distplot(data_binom, hist=True, kde=False)




