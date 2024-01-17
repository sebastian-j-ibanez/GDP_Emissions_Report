import sys
import pandas as pd
import numpy as np
from matplotlib.image import NonUniformImage
import matplotlib.pyplot as plt

country = None
try:
    country = sys.argv[1]
except:
    raise Exception("Program requires the name of a country as an argument (Capitalized). Argument received: {}".format(country))

fileName = './data/em_gdp.csv'
try:
    data = pd.read_csv(fileName)
except:
    raise Exception("'{}' was not found in the dataset.".format(country))

# CHINA - EMISSIONS & GDP
data = data[data['country'] == country]
x = data['year']
y = data['emissions']
z = data['gdp']

fig, ax1 = plt.subplots()

color = '#ff595e'
ln1 = ax1.plot(x, y, color=color)
ax1.set_xlabel('Year')
ax1.set_ylabel('Emissions (Megatons)')
ax1.tick_params(axis='y', labelcolor='black')

ax2 = ax1.twinx()

color = '#8ac926'
ln2 = ax2.plot(x, z, color=color)
ax2.set_xlabel('Year', color=color)
ax2.set_ylabel('GDP (USD)', labelpad=10)
ax2.tick_params(axis='y', labelcolor='black')

lns = ln1 + ln2

plt.legend(lns, ['Emissions', 'GDP'])
plt.title('{}\'s Yearly Emissions and GDP'.format(country))
plt.show()