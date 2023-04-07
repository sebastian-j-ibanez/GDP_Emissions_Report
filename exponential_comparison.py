import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as metrics

data = pd.read_csv('em_gdp.csv')
data = data[data['country'] == 'Canada']

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

canada_emissions_mse = metrics.mean_squared_error(y, predicted_y)
print("Emissiosn MSE:", canada_emissions_mse)

canada_gdp_mse = metrics.mean_squared_error(z, predicted_z)
print("GDP MSE:", canada_gdp_mse)

df = pd.DataFrame({})

plt.bar(x, y, color='#ff595e')
plt.show()