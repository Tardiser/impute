import pandas as pd

# Importing the csv file as a pandas dataframe.
dailyVaccinations = pd.read_csv("country_vaccination_stats.csv")

# Inspecting the dataframe.
print(dailyVaccinations.head())

# Grouping by country to get the minimum for each. 
dvgrouped = dailyVaccinations.groupby("country")['daily_vaccinations'].min()

# Inspecting the minimum vaccination numbers for each country.
print(dvgrouped.head())

# Filling the missing values with minimum values for each country mapped by the country column. 
dailyVaccinations['daily_vaccinations'].fillna(dailyVaccinations['country'].map(dvgrouped), inplace=True)

# Inspecting the imputed dataframe.
print(dailyVaccinations.head())

# Checking to see if there are any country remained with missing values.
print(dailyVaccinations[dailyVaccinations["daily_vaccinations"].isna()])

# Imputing the remaining missing values with 0.
dailyVaccinations['daily_vaccinations'].fillna(0, inplace=True)
print(dailyVaccinations[dailyVaccinations["daily_vaccinations"].isna()])

# Uncomment to export the dataframe to a csv file for further usage.
#dailyVaccinations.to_csv("country_vaccination_stats_imputed.csv",sep = ",", index = False)