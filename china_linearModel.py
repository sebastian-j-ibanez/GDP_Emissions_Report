import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set(style="white", color_codes=True)

#Emissions
data = pd.read_csv('em_gdp.csv', index_col=0)

#Get only China's data
data = data[data['country'] == 'China']
data = data[data['year'] <= 2020]
data = data[['year','gdp','emissions']]
#plt.plot(data['year'], data['emissions'], color='red')


emissions = data[['emissions']]
year = data[['year']]

print(emissions)

#Predict
emissions = data[['emissions']].to_numpy()
year = data[['year']].to_numpy()
m, b = np.polyfit(emissions, year, 1)
plt.plot(emissions, m * emissions + b, color='green')
plt.show()