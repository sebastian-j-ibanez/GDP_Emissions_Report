import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as metrics

fig, ax = plt.subplots()

data = pd.read_csv('em_gdp.csv')
data = data[data['country'] == 'Canada']

x = data['year'].to_numpy()
y = data['gdp'].to_numpy()
z = data['emissions'].to_numpy()

log_y = np.log(y)
log_z = np.log(z)

curve_fit = np.polyfit(x, log_y, 1)
print(curve_fit)

curve_fit_x = round(curve_fit[0], 2)
curve_fit_y = round(curve_fit[1], 2)

predicted_y = np.exp(curve_fit_y) * np.exp(curve_fit_x * x)

mse = metrics.mean_squared_error(y, predicted_y)
print("MSE:", mse)
rmse = math.sqrt(mse)
print("RMSE:", rmse)

ax.plot(x, y)
ax.set_ylabel('GDP')
ax.set_xlabel('Year', color='blue')

ax2 = ax.twinx()
ax2.plot(x, predicted_y, color='red')
ax2.set_ylabel('Predicted GDP')

plt.title('Canada Exponential Model')
plt.show()