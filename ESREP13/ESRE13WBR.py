# PART A -- Energy indicators file is a list of indicators of energy supply and renewable electricity production from the United Nations for the year 2013.

# N O T E : this is an Excel file, and not a comma separated values file; exclude the footer and header information from the data file. 

import matplotlib as plt
import numpy as np 
import pandas as pd
import re


# Energy Supply and Renewable Electricity Production Dataset

Energy = pd.read_excel('/home/aspphem/Desktop/xls/Energy_Indicators.xls', sheet_name = 'Energy', header=17, skipfooter=38) # sheet_name = 0 or index_col = 0; skip header and footer
    #print(Energy.head()) # dataset preview
    #print(Energy.keys()) # column names

Energy = Energy.drop(['Unnamed: 0', 'Unnamed: 1'], axis=1) # drop first two columns; columns -- axis = 1
Energy = Energy.rename(columns={'Unnamed: 2': 'Country', 'Petajoules': 'Energy Supply', 'Gigajoules': 'Energy Supply per Capita', '%': '% Renewable'}) # rename columns
Energy = Energy.replace('...', np.nan) # replace '...' entries with 'NaN' values

Supply_Converted = Energy['Energy Supply'].apply(lambda x: x*(10**6)) # convert unities 
Energy['Energy Supply'] = Supply_Converted # replace Energy Supply column in PJ with Energy Supply column in GJ

# Cleaning Country column entries with REGEX.

def country_names(Country):
    if re.search(r'([\D]*)[\d+]', Country): # search for country names with a digits characters
        up_name = re.findall(r'([\D]*)[\d+]', Country) # drop non-digits characters from those that are digits (e.g. 'Portugal18' to 'Portugal')
        return up_name[0] # updated country name
    elif re.search(r'([\D]*) \(', Country): # search for country names with a parenthesis in their name
        up_name = re.findall(r'([\D]*) \(', Country) # drop parenthesis field from the country name (e.g. 'Iran (Islamic Republic of)' to 'Iran')
        return up_name[0] # updates country  name
    else:
        return Country
    
Energy['Country'] = Energy['Country'].apply(country_names) # apply 'country_names' function to Country column

New_Country = Energy['Country'].replace({'Republic of Korea': 'South Korea', 'United States of America': 'United States', 'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom', 'China, Hong Kong Special Administrative Region': 'Hong Kong', 'Viet Nam': 'Vietnam'}) # rename countries 
Energy['Country'] = New_Country # replace Country column with renamed Country column

    #print(Energy.head()) # dataset preview 
    #print(Energy.keys()) # column names


# World Bank Dataset

GDP = pd.read_csv('/home/aspphem/Desktop/CSV/world_bank.csv', header=4) # load World Bank GDP dataset; skip header

GDP = GDP.rename(columns={'Country Name': 'Country'}) # rename columns

New_Country_GDP = GDP['Country'].replace({'Korea, Rep.': 'South Korea', 'Iran, Islamic Rep.': 'Iran', 'Hong Kong SAR, China': 'Hong Kong'}) # rename countries
GDP['Country'] = New_Country_GDP # replace Country Name column with renamed Country Name column 


# Sciamgo Journal and Country Rank Data for Energy Engineering and Power Technology

ScimEn = pd.read_excel('/home/aspphem/Desktop/xls/scimagojr-3.xlsx', sheet_name = 0)
    

# Joining datasets -- Energy, GDP and ScimEn

SciGDP = pd.merge(GDP, ScimEn, how='outer', on='Country')
DataFrame = pd.merge(Energy, SciGDP, how='outer', on='Country')
DataFrame = DataFrame.set_index('Country') # set 'Country' column to index

Updated_DataFrame = DataFrame.filter(items=['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']) # filter by columns we are interested in

Relevant_DataFrame = Updated_DataFrame[Updated_DataFrame['Rank']<16].sort_values(by=['Rank']) # filter and sort data by rank (top 15 countries by 'Scimagojr' rank); rank 1 through 15

print(Relevant_DataFrame.head()) # dataframe preview (first five rows)
print(Relevant_DataFrame.keys()) # column list
print("DataFrame shape: ", Relevant_DataFrame.shape) # dataframe shape (15, 20) == (15 rows, 20 columns)

# PART B -- When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?

Outer_SciGDP = pd.merge(GDP, ScimEn, how='outer', on='Country')
Outer_DataFrame = pd.merge(Energy, Outer_SciGDP, how='outer', on='Country').set_index('Country') 
print("Outer full join: ", Outer_DataFrame.shape)

Inner_SciGDP = pd.merge(GDP, ScimEn, how='inner', on='Country')
Inner_DataFrame = pd.merge(Energy, Inner_SciGDP, how='inner', on='Country').set_index('Country') 
print("Inner join: ", Inner_DataFrame.shape)

print(len(Outer_DataFrame)-len(Inner_DataFrame))

# PART C -- What are the top 15 countries for average GDP over the last 10 years?

Country_GDP = Relevant_DataFrame.iloc[:,[10,11,12,13,14,15,16,17,18,19]]
avgGDP = Country_GDP.mean(axis=1, skipna=True).sort_values(ascending=False) 
print(avgGDP, type(avgGDP)) # Series

# PART D -- By how much had the GDP changed over the 10 years span for the country with the 6th largest average GDP?

Country = avgGDP.index[5] # country with the 6th largest average GDP
UK = Country_GDP.iloc[3] # United Kingdom GDP entries from 2006 to 2015
UK_GDP = Country_GDP.iloc[3,9] - Country_GDP.iloc[3,0] # GDP 2006 value - GDP 2015 value
print(UK_GDP)

# PART E -- What is the mean energy supply per capita?

Mean_Energy_Supply = Relevant_DataFrame['Energy Supply per Capita'].mean(axis=0, skipna=True) # Relevant_DataFrame.iloc[:,8]
print(Mean_Energy_Supply)

# PART F -- What country has the maximum % Renewable and what is the percentage?

# N O T E: Should return a tuple with the name of the country and the percentage.

Country_Renewable = Relevant_DataFrame['% Renewable'].sort_values(ascending=False)
Max_Renewable = (Country_Renewable.index[0], Country_Renewable[0]) # tuple(country name, maximum '% renewable' value)
print(Max_Renewable, type(Max_Renewable))

# PART G -- Create a new column that is the ratio of Self-Citations to Total Citations. What is the maximum value for this new column, and what country has the highest ratio?

# N O T E: Should return a tuple with the name of the country and the ratio.
    
Citations = (Relevant_DataFrame['Self-citations']/Relevant_DataFrame['Citations']).sort_values(ascending=False)
Max_Ratio = (Citations.index[0], Citations[0]) # tuple(country name, highest ratio)
print(Max_Ratio, type(Max_Ratio))

# PART H -- Create a column that estimates the population using Energy Supply and Energy Supply per Capita. What is the third most populous country according to this estimate? 

Third_Country = (Relevant_DataFrame['Energy Supply']/Relevant_DataFrame['Energy Supply per Capita']).sort_values(ascending=False).index[2]
print(Third_Country)

# PART I -- Create a column that estimates the number of citable documents per person. What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the .corr() method; Pearson's correlation.

Population = (Relevant_DataFrame['Energy Supply']/Relevant_DataFrame['Energy Supply per Capita']) # population estimate
Documents = Relevant_DataFrame['Citable documents']/Population # number of citable documents per capita
DocEn = pd.concat([Relevant_DataFrame['Energy Supply per Capita'], Documents], axis=1)
DocEn.rename(columns={0: "Documents per Capita"}, inplace=True)
print(DocEn.corr(method='pearson'))

# PART J -- Create a new column with a 1 if the contry's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.

def classify(Series):
    x = np.median(Relevant_DataFrame['% Renewable']) # median value
    if Series >= x: # return 1 if the entry is at or above the median value
        return 1 
    return 0 # return 0 if the entry is below the median value

HighRenew = Relevant_DataFrame['% Renewable'].apply(classify) # applying classify function to '% Renewable' column

print(HighRenew)

# PART K -- Use the following dictionary to group the Countries by Continent, then create a DataFrame that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.

ContinentDict = {'China': 'Asia', 'United States': 'North America', 'Japan': 'Asia', 'United Kingdom': 'Europe', 'Russian Federation': 'Europe', 'Canada': 'North America', 'Germany': 'Europe', 'India': 'Asia', 'France': 'Europe', 'South Korea': 'Asia', 'Italy': 'Europe', 'Spain': 'Europe', 'Iran': 'Asia', 'Australia': 'Australia', 'Brazil': 'South America'} 

# N O T E: Should return a DataFrame with index named Continent ['Continents'] and columns ['size', 'sum', 'mean', 'std'] 

Population = (Relevant_DataFrame['Energy Supply']/Relevant_DataFrame['Energy Supply per Capita']) # population estimate
Relevant_DataFrame['Estimated Population'] = Population
Relevant_DataFrame['Continent'] = pd.Series(ContinentDict)
Continents = Relevant_DataFrame.groupby("Continent").agg({"Estimated Population":(np.size,np.sum,np.mean,np.std)})
Continents.columns = Continents.columns.droplevel()
print(Continents)

# PART L -- Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?

Renewable = Relevant_DataFrame['% Renewable'] 
Renewable_Bins = pd.cut(Renewable, 5) # cut() function takes as an argument some array-like structure, such as a column of a data frame or a series, and the number of bins to be used, all bins are kept at equal spacing
Relevant_DataFrame['% Renewable Categories'] = Renewable_Bins
ConRenew = Relevant_DataFrame.groupby(['Continent', '% Renewable Categories'])['Continent'].agg(np.size)
print(ConRenew, type(ConRenew), len(ConRenew))

# PART M -- Convert the Population Estimate series to a string with thousands separator (using commas). Use all significant digits (do not round the results).

Population = (Relevant_DataFrame['Energy Supply']/Relevant_DataFrame['Energy Supply per Capita']) # population estimate
StrPop = Population.apply('{:,}'.format)
print(StrPop)


        
    
