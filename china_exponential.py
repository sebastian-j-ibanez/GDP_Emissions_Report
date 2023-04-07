import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as metrics

data = pd.read_csv('em_gdp.csv')
data = data[data['country'] == 'China']

x = data['year'].to_numpy()
y = data['emissions'].to_numpy()
z = data['gdp'].to_numpy()

log_y = np.log(y)
log_z = np.log(z)

curve_fit = np.polyfit(x, log_y, 1)
curve_fit_x = round(curve_fit[0], 3)
curve_fit_y = round(curve_fit[1], 3)
predicted_y = np.exp(curve_fit_y) * np.exp(curve_fit_x * x)

curve_fit = np.polyfit(x, log_z, 1)
curve_fit_x = round(curve_fit[0], 3)
curve_fit_z = round(curve_fit[1], 3)
predicted_z = np.exp(curve_fit_z) * np.exp(curve_fit_x * x)

emissions_mse = metrics.mean_squared_error(y, predicted_y)
print("Emissiosn MSE:", emissions_mse)
emissions_rmse = math.sqrt(emissions_mse)
print("Emissions RMSE:", emissions_rmse)

gdp_mse = metrics.mean_squared_error(z, predicted_z)
print("GDP MSE:", gdp_mse)
gdp_rmse = math.sqrt(gdp_mse)
print("GDP RMSE:", gdp_rmse)

plt.subplot(2, 1, 1)
plt.plot(x, y, color='#ff595e')
plt.plot(x, predicted_y, color='#ffb703', linestyle='--')
plt.title('China\'s Emissions - Exponential Predicted Model')
plt.legend(['Actual', 'Predicted'])
plt.xlabel('Year')
plt.ylabel('Emissions')

plt.subplots_adjust(hspace=0.75)
plt.subplot(2, 1, 2)
plt.plot(x, z, color='#8ac926')
plt.plot(x, predicted_z, color='#ffb703', linestyle='--')
plt.title('China\'s GDP - Exponential Predicted Model')
plt.legend(['Actual', 'Predicted'])
plt.xlabel('Year')
plt.ylabel('GDP')

plt.show()