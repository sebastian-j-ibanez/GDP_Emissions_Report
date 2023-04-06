import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white", color_codes=True)

#Emissions
data = pd.read_csv('em_gdp.csv')

#Get only Mexico's data
data = data[data['country'] == 'Mexico']
plt.plot(data['year'], data['emissions'], color='red')

#Data all from 1960-2020
data = data[data['year'] <= 2020]

#Only use year, gdp, and emissions columns
data = data[['year','gdp','emissions']]

yearly_change_em = pd.DataFrame()
yearly_change_em['year'] = data['year']
yearly_change_em['pct_em'] = data['emissions'].pct_change()

yearly_change_gdp = pd.DataFrame()
yearly_change_gdp['year'] = data['year']
yearly_change_gdp['pct_gdp'] = data['gdp'].pct_change()

avg_chng_gdp = yearly_change_gdp['pct_gdp'].mean()
avg_chng_em = yearly_change_em['pct_em'].mean()

#Predict
predicted_em = pd.DataFrame()
predicted_em_years = [1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
predicted_em_values = []
# Loop for 10 years, predicting 2011 - 2020
# emissions * (1 + yearly average emissions change) 10,000 * (1 + 0.05)


temp = data[data['year'] == 1960]
temp2 = temp['emissions']
emissions = temp2.iloc[0]

for x in predicted_em_years:
    em = emissions * (1 + avg_chng_em)
    emissions = em
    predicted_em_values.append(em)

df = pd.DataFrame(predicted_em_values, columns=['emissions'])
df = df.mean()
print(df)
print(data['emissions'].mean())

plt.plot(predicted_em_years, predicted_em_values, color='green')

plt.title('Mexico Emissions Nonlinear Model')
plt.legend(['Emissions', 'Predicted Emissions'])
plt.xlabel('Year', labelpad=10)
plt.ylabel('Emissions (Million Metric Tons)', labelpad=10)
plt.show()