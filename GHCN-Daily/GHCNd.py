# PART A -- Loading data set and transform the data into C degrees, then extract all of the rows which have minimum or maximum temperatures.

import pandas as pd
import re
import numpy as np
from datetime import datetime

Weather_Observations = pd.read_csv("/home/aspphem/Desktop/CSV/GHCNd.csv")
print(Weather_Observations.head()) # data set preview
print(Weather_Observations.keys()) # column names

Transformed_Values = Weather_Observations['Data_Value'].apply(lambda x: x/10) # Data values are stored in integer representation rather than float

Weather_Observations['Data_Value'] = Transformed_Values # replace Data_Value column with Transformed_Values column

Weather_Observations = Weather_Observations.rename(columns={'Data_Value': 'Degrees_C'}) # rename Data_Value column to Degrees_C

print(Weather_Observations.head(), Weather_Observations.shape)

Filtered_Dates = Weather_Observations['Date'].apply(lambda x: 1 if re.search(r'\d+\-+02+\-+29', x) else x) # identify leap year dates

Weather_Observations['Date'] = Filtered_Dates # replace columns

Observations = Weather_Observations[Weather_Observations['Date'] != 1] # drop leap year dates

Max_Observations = Observations[Observations['Element'] == 'TMAX']
Min_Observations = Observations[Observations['Element'] == 'TMIN']

print(Max_Observations.head(),"\n", 
"DataFrame object with {} entries and {} columns".format(Max_Observations.shape[0], Max_Observations.shape[1]))

print(Min_Observations.head(),"\n",
"DataFrame object with {} entries and {} columns".format(Min_Observations.shape[0], Min_Observations.shape[1]))

# PART B -- In order to visualize the data we would plot the min and max data for each day of the year between the years 2005 and 2014 across all weather stations. But we also need to find out when the min or max temperature in 2015 falls below the min or rises above the max for the previous decade.

Max_TDate = Max_Observations.groupby('Date').aggregate('max').reset_index() # 3 columns, 4015 entries
Min_TDate = Min_Observations.groupby('Date').aggregate('min').reset_index() # 3 columns, 4015 entries

# PART C -- Separate out the data for 2015. Then you can use the Pandas groupby function to find the max and min of the temperature data for each day of the year for the 2005-2014 data.

# 2015 year data frames (max and min observations)

    # Max Observations DataFrame

Max_TDate_2015 = Max_TDate.copy() # make a new copy for 2015 data

Max_Y2015 = Max_TDate['Date'].apply(lambda x: x if re.search(r'2015+\-+\d+\-+\d', x) else 1) # identify 2015 year dates

Max_TDate_2015['Date'] = Max_Y2015 # replace columns to apply Boolean mask

Max_Observations_Y2015 = Max_TDate_2015[Max_TDate_2015['Date'] != 1] # 2015 year observations; 365 entries

    # Min Observations DataFrame

Min_TDate_2015 = Min_TDate.copy()

Min_Y2015 = Min_TDate['Date'].apply(lambda x: x if re.search(r'2015+\-+\d+\-+\d', x) else 1) 

Min_TDate_2015['Date'] = Min_Y2015 

Min_Observations_Y2015 = Min_TDate_2015[Min_TDate_2015['Date'] != 1]

# 2005 to 2014 data frames (max and min observations)

    # Max Observations DataFrame

Max_Observations_0514 = Max_TDate['Date'].apply(lambda x: 1 if re.search(r'2015+\-+\d+\-+\d', x) else x) # identify 2015 year dates

Max_TDate['Date'] = Max_Observations_0514 # replace columns to apply Boolean mask

Max_Obs_2005_to_2014 = Max_TDate[Max_TDate['Date'] != 1] # drop 2015 year observations; 2005 to 2014 observations, 3650 entries

    # Min Observations DataFrame

Min_Observations_0514 = Min_TDate['Date'].apply(lambda x: 1 if re.search(r'2015+\-+\d+\-+\d', x) else x) 

Min_TDate['Date'] = Min_Observations_0514

Min_Obs_2005_to_2014 = Min_TDate[Min_TDate['Date'] != 1]

# Max and min temperatures data for each day of the year ***2005-2014 data

Date_YearMonthDay = Max_Obs_2005_to_2014['Date'] # max observations
Date_YearMonthDay_min = Min_Obs_2005_to_2014['Date'] # min observations

def year(Date):
    year = re.findall(r'\d{4}', Date) # get year from 'YYYY-MM-DD' string
    return year[0]
    
DateCol_Y = Date_YearMonthDay.apply(year) # year column
DateCol_Y_min = Date_YearMonthDay_min.apply(year)

def month_day(Date):
    month_day = re.findall(r'\d{2}\-(\d{2}\-\d{2})', Date) # get month and day from 'YYYY-MM-DD' string
    return month_day[0]

DateCol_MD = Date_YearMonthDay.apply(month_day) # month-day column
DateCol_MD_min = Date_YearMonthDay_min.apply(month_day)

    # Max Observations

Max_Obs_2005_to_2014_C = Max_Obs_2005_to_2014.copy() # make a new copy
Max_Obs_2005_to_2014_C['Year'] = DateCol_Y # add year column
Max_Obs_2005_to_2014_C['Month-Day'] = DateCol_MD # add month-day column

Max_Observations_Day = Max_Obs_2005_to_2014_C.drop(['Date'], axis=1) # drop Date column

Max_Observations_per_Day = Max_Observations_Day.groupby('Month-Day').aggregate('max') # max temperature for each day of year; 365 entries
Relevant_Max_Observations = Max_Observations_per_Day.reset_index() # reset index

Relevant_Max_Observations['Date'] = Relevant_Max_Observations[['Year', 'Month-Day']].agg('-'.join, axis=1) # join year and month-day columns in a Date column

Relevant_Max_Observations = Relevant_Max_Observations.drop(['Year'], axis =1) # drop useless columns 
Relevant_Max_Observations = Relevant_Max_Observations.drop(['Month-Day'], axis =1)

Relevant_Max_Observations = Relevant_Max_Observations[['Date', 'ID', 'Element', 'Degrees_C']] # rearrange columns

    #   Min Observations
    
Min_Obs_2005_to_2014_C = Min_Obs_2005_to_2014.copy() 
Min_Obs_2005_to_2014_C['Year'] = DateCol_Y_min
Min_Obs_2005_to_2014_C['Month-Day'] = DateCol_MD_min

Min_Observations_Day = Min_Obs_2005_to_2014_C.drop(['Date'], axis=1) 

Min_Observations_per_Day = Min_Observations_Day.groupby('Month-Day').aggregate('min')
Relevant_Min_Observations = Min_Observations_per_Day.reset_index()

Relevant_Min_Observations['Date'] = Relevant_Min_Observations[['Year', 'Month-Day']].agg('-'.join, axis=1)

Relevant_Min_Observations = Relevant_Min_Observations.drop(['Year'], axis =1)
Relevant_Min_Observations = Relevant_Min_Observations.drop(['Month-Day'], axis =1)

Relevant_Min_Observations = Relevant_Min_Observations[['Date', 'ID', 'Element', 'Degrees_C']] 

print(Relevant_Max_Observations) # Max observations for each day for the 2005-2014 time period; 365 entries

print(Relevant_Min_Observations) # Min observations for each day for the 2005-2014 time period; 365 entries

# PART D -- Plot line graphs of the min and max temperatures for the years 2005 through 2014 and to scatter plot only the daily 2015 temperatures that exceed those values.

Max_Values_15 = Max_Observations_Y2015[['Degrees_C', 'Date']].reset_index()
Max_Values_0514 = Relevant_Max_Observations['Degrees_C'].reset_index()
Max_values = []
Max_dates = []
c = 0
for x in range(len(Max_Values_15['Degrees_C'])):
    if Max_Values_15['Degrees_C'][x] > Max_Values_0514['Degrees_C'][x]:
        Max_values.append(Max_Values_15['Degrees_C'][x])
        Max_dates.append(Max_Values_0514['index'][x])
    else: 
        c += 1
        
Min_Values_15 = Min_Observations_Y2015['Degrees_C'].reset_index()
Min_Values_0514 = Relevant_Min_Observations['Degrees_C'].reset_index()
Min_values = []
Min_dates = []
c = 0
for x in range(len(Min_Values_15['Degrees_C'])):
    if Min_Values_15['Degrees_C'][x] < Min_Values_0514['Degrees_C'][x]:
        Min_values.append(Min_Values_15['Degrees_C'][x])
        Min_dates.append(Min_Values_0514['index'][x])
    else: 
        c += 1

import matplotlib.pyplot as plt
from calendar import month_abbr

plt.figure(figsize=(10,6))

plt.xlabel('Month', fontsize=10) # x label
plt.ylabel('Temperature (°C)', fontsize=10) # y label
plt.title('Daily Records for Temperatures Between 2005-2014', fontsize=13) # title chart

plt.plot(Relevant_Max_Observations['Degrees_C'], c = 'red', label = 'Maximum Observations', alpha=0.75)
plt.plot(Relevant_Min_Observations['Degrees_C'], c = 'blue', label = 'Minimum Observations', alpha=0.75)

plt.scatter(Max_dates, Max_values, c = 'black', label = 'Maximum Observations in 2015')
plt.scatter(Min_dates, Min_values, c = 'green', label = 'Minimum Observations in 2015')

plt.gca().fill_between(range(len(Relevant_Max_Observations['Degrees_C'])), Relevant_Max_Observations['Degrees_C'], Relevant_Min_Observations['Degrees_C'], facecolor='#2F99B4', alpha=0.25)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
#plt.legend(loc = 8, fontsize = 8, frameon = False)
plt.legend(bbox_to_anchor=(1, 1), loc='upper center', fancybox=True, shadow=True)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Aug', 'Oct', 'Nov', 'Dec']

plt.locator_params(axis='x', nbins=11)
ax = plt.subplot()
ax.set_xticklabels(months)

plt.show()

