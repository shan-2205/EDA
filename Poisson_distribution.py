
import numpy as np
import pandas as pd
import scipy.stats as stats

school_ages=stats.poisson.rvs(loc=18,mu=35,size=1500)
school_ages