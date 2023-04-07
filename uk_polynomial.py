import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as metrics

data = pd.read_csv('em_gdp.csv')
data = data[data['country'] == 'United Kingdom']

x = data['year'].to_numpy()
y = data['emissions'].to_numpy()
z = data['gdp'].to_numpy()

ymodel = np.poly1d(np.polyfit(x, y, 3))
zmodel = np.poly1d(np.polyfit(x, z, 3))

myline = np.linspace(1960, 2020, 100)

plt.subplot(2, 1, 1)
plt.plot(x, y, color='#ff595e')
plt.plot(myline, ymodel(myline), color='#ffb703', linestyle='--')
plt.title('UK Emissions - Polynomial Predicted Model (3rd Degree)')
plt.legend(['Actual', 'Predicted'])
plt.xlabel('Year')
plt.ylabel('Emissions')

plt.subplots_adjust(hspace=0.75)
plt.subplot(2, 1, 2)
plt.plot(x, z, color='#8ac926')
plt.plot(myline, zmodel(myline), color='#ffb703', linestyle='--')
plt.title('UK GDP - Polynomial Predicted Model (3rd Degree)')
plt.legend(['Actual', 'Predicted'])
plt.xlabel('Year')
plt.ylabel('GDP')
plt.show()