import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics

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

emissions_mse = metrics.mean_squared_error(y, y_line)
print("Emissiosn MSE:", emissions_mse)
emissions_rmse = math.sqrt(emissions_mse)
print("Emissions RMSE:", emissions_rmse)

gdp_mse = metrics.mean_squared_error(z, z_line)
print("GDP MSE:", gdp_mse)
gdp_rmse = math.sqrt(gdp_mse)
print("GDP RMSE:", gdp_rmse)

#Predict
plt.subplot(2, 1, 1)
plt.plot(x, y, color='#ff595e')
plt.plot(x, y_line, color='#ffb703', linestyle='--')
plt.title('China\'s Emissions - Linear Predicted Model')
plt.legend(['Actual', 'Predicted'])
plt.xlabel('Year')
plt.ylabel('Emissions (Megatons)')

plt.subplots_adjust(hspace=0.75)
plt.subplot(2, 1, 2)
plt.plot(x, z, color='#8ac926')
plt.plot(x, z_line, color='#ffb703', linestyle='--')
plt.title('China\'s GDP - Linear Predicted Model')
plt.legend(['Actual', 'Predicted'])
plt.xlabel('Year')
plt.ylabel('GDP (USD)')
plt.show()