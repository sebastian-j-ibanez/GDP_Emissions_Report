import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Emissions
data = pd.read_csv('em_gdp.csv')
data = data[data['country'] == 'China']

x = data['year']
y = data['emissions']
z = data['gdp']

ychange = y.pct_change()
ychange = ychange.fillna(0)
ymean = ychange.mean()

y_m, y_b = np.polyfit(x, y, 1)
y_line = np.polyval([y_m, y_b], x)

z_m, z_b = np.polyfit(x, z, 1)
z_line = np.polyval([z_m, z_b], x)

zchange = z.pct_change()
zchange = zchange.fillna(0)
zmean = zchange.mean()

#Predict
plt.subplot(2, 1, 1)
plt.plot(x, y, color='#ff595e')
plt.plot(x, y_line, color='#ffb703', linestyle='--')
plt.title('China\'s Emissions - Linear Predicted Model')
plt.legend(['Actual', 'Predicted'])
plt.xlabel('Year')
plt.ylabel('Emissions')

plt.subplots_adjust(hspace=0.75)
plt.subplot(2, 1, 2)
plt.plot(x, z, color='#8ac926')
plt.plot(x, z_line, color='#ffb703', linestyle='--')
plt.title('China\'s GDP - Linear Predicted Model')
plt.legend(['Actual', 'Predicted'])
plt.xlabel('Year')
plt.ylabel('GDP')
plt.show()