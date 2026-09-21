#loading the csv data
import pandas as pd
df = pd.read_csv("exoplanets.csv", comment="#") #tells pandas to ignore any line starting with #
#print (df.head())
#print(df.columns)
#print(df.columns.tolist())

#"for each year, how many exoplanets were found by each method?"
import matplotlib.pyplot as plt
counts_by_year_method= df.groupby(['disc_year', 'discoverymethod']).size().unstack(fill_value=0)
#print (counts_by_year_method)
#turning it into plot
counts_by_year_method.plot(kind='bar', stacked=True, figsize=(14, 6))
plt.xlabel("Discovery Year")
plt.ylabel("Number of Exoplanets Discovered")
plt.title("Exoplanet Discoveries by Method Over Time")
plt.show()
