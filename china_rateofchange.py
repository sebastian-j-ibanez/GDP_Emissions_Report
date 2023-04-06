import pandas as pd
import numpy as np

from matplotlib.image import NonUniformImage
import matplotlib.pyplot as plt

data = pd.read_csv('em_gdp.csv')

data = data[data['country'] == 'China']
x = data['year']
y = data['emissions']
z = data['gdp']

ychange = y.pct_change()
zchange = z.pct_change()

ychange = ychange.fillna(0)
zchange = zchange.fillna(0)

ymean = ychange.mean()
zmean = zchange.mean()
print('Emissions: ' + ymean.astype(str))
print('GDP: ' + zmean.astype(str))

plt.plot(x, ychange, color='red')
plt.plot(x, zchange, color='green')

plt.legend(['Emissions', 'GDP'])
plt.title('China Yearly Emissions and GDP')
plt.show()