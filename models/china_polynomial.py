import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as metrics

data = pd.read_csv('./data/em_gdp.csv')
data = data[data['country'] == 'China']

x = data['year'].to_numpy()
y = data['emissions'].to_numpy()
z = data['gdp'].to_numpy()

yPredicted = np.polyfit(x, y, 3)
zPredicted = np.polyfit(x, z, 3)

ymodel = np.poly1d(yPredicted)
zmodel = np.poly1d(zPredicted)

yPredicted = ymodel(x)
yr2 = metrics.r2_score(y, yPredicted)
print('China\'s Emissions R2: ', yr2)

zPredicted = zmodel(x)
zr2 = metrics.r2_score(z, zPredicted)
print('China\'s GDP R2: ', zr2)

myline = np.linspace(1960, 2020, 100)

plt.subplot(2, 1, 1)
plt.plot(x, y, color='#ff595e')
plt.plot(myline, ymodel(myline), color='#ffb703', linestyle='--')
plt.title('China\'s Emissions - Polynomial Predicted Model (3rd Degree)')
plt.legend(['Actual', 'Predicted'])
plt.xlabel('Year')
plt.ylabel('Emissions (Megatons)')

plt.subplots_adjust(hspace=0.75)
plt.subplot(2, 1, 2)
plt.plot(x, z, color='#8ac926')
plt.plot(myline, zmodel(myline), color='#ffb703', linestyle='--')
plt.title('China\'s GDP - Polynomial Predicted Model (3rd Degree)')
plt.legend(['Actual', 'Predicted'])
plt.xlabel('Year')
plt.ylabel('GDP (USD)')
plt.show()