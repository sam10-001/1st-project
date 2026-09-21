#loading the csv data
import pandas as pd
df = pd.read_csv("exoplanets.csv", comment="#")
# above line tells pandas to ignore any line starting with hashtag
#print (df.head())
#print(df.columns)
#print(df.columns.tolist())

#"for each year, how many exoplanets were found by each method?"
import matplotlib.pyplot as plt
'''counts_by_year_method= df.groupby(['disc_year', 'discoverymethod']).size().unstack(fill_value=0)
#print (counts_by_year_method)
#turning it into plot
counts_by_year_method.plot(kind='bar', stacked=True, figsize=(14, 6))
plt.xlabel("Discovery Year")
plt.ylabel("Number of Exoplanets Discovered")
plt.title("Exoplanet Discoveries by Method Over Time")
plt.show()'''

#"Do planets with longer orbital periods tend to be more massive?"
'''plt.scatter(df['pl_orbper'],df['pl_bmasse'], alpha=0.3,s=10) #pl_orbper=orbital period, pl_bmasse=planet mass
plt.xscale('log')
plt.yscale('log')
#added log scale to evenly zoom out data so it doesnt get squished 
plt.xlabel("Orbital c")
plt.ylabel("Planet Mass (Earth masses)")
plt.title("Orbital Period vs Planet Mass")
plt.show()
#got a messy plot with some clusters revealing there could be a third variable, possibly discovery method

#trying the plot again by method and resolve the mess
fig,ax=plt.subplots(figsize=(10,7))'''

'''for method in df['discoverymethod'].unique():
    subset=df[df['discoverymethod']==method]
    ax.scatter(subset['pl_orbper'],subset['pl_bmasse'],alpha=0.3,s=10,label=method)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("Orbital Period (days, log scale)")
ax.set_ylabel("Planet Mass (Earth masses, log scale)")
ax.set_title("Orbital Period vs Planet Mass, by Discovery Method")
ax.legend(markerscale=3, fontsize=8)
plt.show()'''

#confirming no relation numerically
correlation = df['pl_orbper'].corr(df['pl_bmasse'])
print("the Pearson correlation coefficient between orbital period and planet mass is : ",correlation)
print("shows that orbital period and planet mass have virtually no linear relationship in this dataset")

#testing kepler's 3rd law graphically (T^2 propto a^3)
plt.scatter(df['pl_orbsmax'],df["pl_orbper"],alpha=0.3, s=10)
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Orbital distance/ Semi major axis (AU, log scale)")
plt.ylabel("Orbital Period (days, log scale)")
plt.title("Orbital Period vs Orbital Distance")
plt.show()
# testing it numerically
import numpy as np
#drop rows with missing values in either column first
valid=df[['pl_orbsmax','pl_orbper']].dropna()
log_a=np.log10(valid['pl_orbsmax'])
log_T=np.log10(valid['pl_orbper'])
slope, intercept=np.polyfit(log_a,log_T,1)
print(f"Slope: {slope:.3f}")