# First, we'll import pandas, a data processing and CSV file I/O library
import pandas as pd
import numpy as np

# We'll also import seaborn, a Python graphing library
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")
import seaborn as sns
from matplotlib.image import NonUniformImage
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)


#Emissions
emissions = pd.read_csv('emissions.csv')

emissions = emissions.drop('Per Capita', 1)
emissions = emissions.drop('Other', 1)
emissions = emissions.drop('Flaring', 1)
emissions = emissions.drop('Cement', 1)
emissions = emissions.drop('Gas', 1)
emissions = emissions.drop('Oil', 1)
emissions = emissions.drop('Coal', 1)
emissions = emissions.drop('ISO 3166-1 alpha-3', 1)

#remove global and international transport rows to get just each countries
emissions = emissions[emissions["Country"] != "Global"]
emissions = emissions[emissions["Country"] != "International Transport"]

sorted = emissions[emissions["Year"] == 2020]
sorted = sorted.sort_values("Total")

emissions = emissions[emissions["Year"] <= 2020]
emissions =emissions[emissions["Year"] >= 1960]
emissions = emissions.drop('Year', 1)

usa_em = emissions[emissions["Country"] == "USA"]
usa_em = usa_em.drop('Country', 1)
china_em = emissions[emissions["Country"] == "China"]
china_em = china_em.drop('Country', 1)
india_em = emissions[emissions["Country"] == "India"]
india_em = india_em.drop('Country', 1)
germany_em = emissions[emissions["Country"] == "Germany"]
germany_em = germany_em.drop('Country', 1)
russia_em = emissions[emissions["Country"] == "Russia"]
russia_em = russia_em.drop('Country', 1)
japan_em = emissions[emissions["Country"] == "Japan"]
japan_em = japan_em.drop('Country', 1)
uk_em = emissions[emissions["Country"] == "United Kingdom"]
uk_em = uk_em.drop('Country', 1)

#GDP
pd.set_option('display.float_format', '{:.2f}'.format)
gdp = pd.read_csv('gdp.csv')

gdp = gdp.drop('gdp_percent_global', 1)
gdp = gdp.drop('inflation_percent', 1)
gdp = gdp.drop('gdp_deflator', 1)
gdp = gdp.drop('real_gdp', 1)
gdp = gdp.drop('year_country', 1)

gdp = gdp[gdp["year"] >= 1960]

gdp = gdp.drop('year', 1)

usa_gdp = gdp[gdp["country"] == "the United States"]
usa_gdp = usa_gdp.drop('country', 1)
china_gdp = gdp[gdp["country"] == "China"]
china_gdp = china_gdp.drop('country', 1)
india_gdp = gdp[gdp["country"] == "India"]
india_gdp = india_gdp.drop('country', 1)
germany_gdp = gdp[gdp["country"] == "Germany"]
germany_gdp = germany_gdp.drop('country', 1)
russia_gdp = gdp[gdp["country"] == "Russia"]
russia_gdp = russia_gdp.drop('country', 1)
japan_gdp = gdp[gdp["country"] == "Japan"]
japan_gdp = japan_gdp.drop('country', 1)
uk_gdp = gdp[gdp["country"] == "United Kingdom"]
uk_gdp = uk_gdp.drop('country', 1)


x = usa_gdp['gdp']
y = usa_em['Total']

x1 = uk_gdp['gdp']
y1 = uk_em['Total']
#plt.scatter(x, y)
plt.scatter(x1, y1)
print(len(x1))
print(len(y1))

plt.show()