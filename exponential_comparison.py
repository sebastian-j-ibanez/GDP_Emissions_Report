import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white", color_codes=True)

# Read data from CSV file
data = pd.read_csv('em_gdp.csv')

# Select data only for China, India, and the United States
countries = ['China', 'India', 'United States']
data = data[data['country'].isin(countries)]

# Plot emissions data for each country
g = sns.FacetGrid(data, col="country", col_wrap=3)
g.map(plt.plot, "year", "emissions", marker=".")

# Select data for years 1960-2020
data = data[data['year'] <= 2020]

# Select only year, gdp, and emissions columns
data = data[['year', 'gdp', 'emissions']]

# Calculate average yearly percentage change in emissions and GDP
yearly_change_em = pd.DataFrame()
yearly_change_em['year'] = data['year']
yearly_change_em['pct_em'] = data['emissions'].pct_change()

yearly_change_gdp = pd.DataFrame()
yearly_change_gdp['year'] = data['year']
yearly_change_gdp['pct_gdp'] = data['gdp'].pct_change()

avg_chng_gdp = yearly_change_gdp['pct_gdp'].mean()
avg_chng_em = yearly_change_em['pct_em'].mean()

# Predict emissions for each country
predicted_em = pd.DataFrame()
predicted_em_years = list(range(1960, 2021))
for country in countries:
    country_data = data[data['country'] == country]
    emissions = country_data['emissions'].iloc[0]
    predicted_em_values = []
    for year in predicted_em_years:
        em = emissions * (1 + avg_chng_em)
        emissions = em
        predicted_em_values.append(em)
    predicted_em[country] = predicted_em_values

# Compare means of predicted emissions for each country
predicted_em_means = predicted_em.mean()
print(predicted_em_means)
