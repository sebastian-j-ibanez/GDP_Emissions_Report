# First, we'll import pandas, a data processing and CSV file I/O library
import pandas as pd

# We'll also import seaborn, a Python graphing library
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

data = pd.read_csv('emissions.csv')

print(data.head())
print(data.info())

#remove global and international transport rows to get just each countries
data = data[data["Country"] != "Global"]
data = data[data["Country"] != "International Transport"]

sorted = data[data["Year"] == 2020]
sorted = sorted.sort_values("Total")
print(sorted)

#just canada
usa = data[data["Country"] == "USA"]
china = data[data["Country"] == "China"]
india = data[data["Country"] == "India"]
germany = data[data["Country"] == "Germany"]
russia = data[data["Country"] == "Russia"]
japan = data[data["Country"] == "Japan"]
uk = data[data["Country"] == "United Kingdom"]

usa = usa[usa["Year"] >= 1850]
china = china[china["Year"] >= 1850]
india = india[india["Year"] >= 1850]
germany = germany[germany["Year"] >= 1850]
russia = russia[russia["Year"] >= 1850]
japan = japan[japan["Year"] >= 1850]
uk = uk[uk["Year"] >= 1850]


plt.plot(usa["Year"], usa["Total"], label = "USA")
plt.plot(china["Year"], china["Total"], label = "China")
plt.plot(india["Year"], india["Total"], label = "India")
plt.plot(germany["Year"], germany["Total"], label = "Germany")
plt.plot(russia["Year"], russia["Total"], label = "Russia")
plt.plot(japan["Year"], japan["Total"], label = "Japan")
plt.plot(uk["Year"], uk["Total"], label = "UK")
plt.title("Yearly Emissions")
plt.ylabel("Emissions - Tons")
plt.xlabel("Year")
plt.legend()
plt.show()