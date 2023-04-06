import pandas as pd

# We'll also import seaborn, a Python graphing library
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

pd.set_option('display.float_format', '{:.2f}'.format)
data = pd.read_csv('gdp.csv')
print(data.head())
print(data.info())

recent = data[data["year"] >= 1960]

usa = data[data["country"] == "the United States"]
china = data[data["country"] == "China"]
india = data[data["country"] == "India"]
germany = data[data["country"] == "Germany"]
russia = data[data["country"] == "Russia"]
japan = data[data["country"] == "Japan"]
uk = data[data["country"] == "United Kingdom"]

plt.plot(usa["year"], usa["gdp"], label = "USA")
plt.plot(china["year"], china["gdp"], label = "China")
plt.plot(india["year"], india["gdp"], label = "India")
plt.plot(germany["year"], germany["gdp"], label = "Germany")
plt.plot(russia["year"], russia["gdp"], label = "Russia")
plt.plot(japan["year"], japan["gdp"], label = "Japan")
plt.plot(uk["year"], uk["gdp"], label = "UK")
plt.title("Yearly GDP")
plt.ylabel("Emissions - Tons")
plt.xlabel("Year")
plt.legend()
plt.show()