import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set(style="white", color_codes=True)

#Emissions
data = pd.read_csv('em_gdp.csv')
data = data[['country', 'emissions', 'gdp']]

usData = data[data['country'] == 'the United States']
ukData = data[data['country'] == 'United Kingdom']
canadaData = data[data['country'] == 'Canada']
chinaData = data[data['country'] == 'China']
indiaData = data[data['country'] == 'India']
brazilData = data[data['country'] == 'Brazil']

usCorr = usData['emissions'].corr(usData['gdp'])
ukCorr = ukData['emissions'].corr(ukData['gdp'])
canadaCorr = canadaData['emissions'].corr(canadaData['gdp'])
chinaCorr = chinaData['emissions'].corr(chinaData['gdp'])
indiaCorr = indiaData['emissions'].corr(indiaData['gdp'])
brazilCorr = brazilData['emissions'].corr(brazilData['gdp'])

fig, ax = plt.subplots(figsize=(8, 8))

correlationList = [usCorr, ukCorr, canadaCorr, chinaCorr, indiaCorr, brazilCorr]
countryList = ['United States', 'United Kingdom', 'Canada', 'China', 'India', 'Brazil']

corrDF = pd.DataFrame({'Country': countryList, 'Correlation': correlationList})
bars = plt.bar(corrDF['Country'], corrDF['Correlation'])
ax.bar_label(bars, padding=-20, color='white', fontsize=12, label_type='edge', fmt='%.2f' ,fontweight='bold')

plt.ylim(-1, 1)
plt.xticks(rotation=30, horizontalalignment="center")
plt.axhline(y = 0, color='black', linestyle = '-')
plt.ylabel('Correlation')
plt.xlabel('Country', labelpad=-10)
plt.title('Correlation Between GDP and Emissions (1960-2020)', pad=20)
plt.show()