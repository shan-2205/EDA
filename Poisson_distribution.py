#Question solution on POisson
from scipy.stats import poisson
poisson.pmf(3,2)











import numpy as np
import pandas as pd
import scipy.stats as stats

# Generating Random Numbers which follows poisson distribution path
school_ages=stats.poisson.rvs(mu=35,size=1500)
sns.distplot(school_ages)














