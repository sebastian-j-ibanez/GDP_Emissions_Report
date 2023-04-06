# manage data and fit
import pandas as pd
import numpy as np

# first part with least squares
from scipy.optimize import curve_fit

# second part about ODR
from scipy.odr import ODR, Model, Data, RealData

# style and notebook integration of the plots
import seaborn as sns
#matplotlib inline
sns.set(style="whitegrid")

#Emissions
data = pd.read_csv('em_gdp.csv')
data = data[data['country'] == 'China']
data = data[data['year'] <= 2020]
data = data[['year','gdp','emissions']]