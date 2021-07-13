import pandas as pd

# Importing the csv file as a pandas dataframe.
dailyVaccinations = pd.read_csv("country_vaccination_stats_imputed.csv")

# Inspecting the dataframe.
print(dailyVaccinations.head())

# Grouping by country to get the median of each. 
dvGrouped = dailyVaccinations.groupby("country").median()
print(dvGrouped.head())

# Ordering by median daily vaccinations and listing the top 3.
dvGroupedSorted = dvGrouped.sort_values(by = ['daily_vaccinations'], ascending = False)
print(dvGroupedSorted.head(3))

