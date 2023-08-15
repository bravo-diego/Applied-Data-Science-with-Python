# Date/Time Functionality

# Pandas has four main time related classes; 'Timestamp', 'DateTimeIndex', 'period', and 'PeriodIndex'.

import pandas as pd
import numpy as np

# Timestamp

print(pd.Timestamp('12/20/2023 10:05AM'))
print(type(pd.Timestamp('9/1/2023 10:05AM')))

print(pd.Timestamp(2023, 12, 20, 10, 5, 30)) # timestamp by passing multiple parameters such as year, month, date, hour, minute, second, separately

# Timestamp also has some useful attributes, such as isoweekday(), which shows the weekday of the timestamp.

print(pd.Timestamp(2023, 12, 20, 10, 5, 30).isoweekday()) # 1 represents Monday and 7 represents Sunday

print(pd.Timestamp(2023, 12, 20, 10, 5, 30).month, "\n") # you can find extract the specific year, month, day, hour, minute, second from a timestamp

# Period

# Suppose we weren't interested in a specific point in time and instead wanted a span of time; this is where the Period class comes into play. Period represents a single time span, such as a specific day or month.

print(pd.Period('1/2023'))
print(type(pd.Period('1/2023')))

# Period objects represent the full timespan that you specify. Arithmetic on period is very easy and intuitive, for instance if we want to find out 5 months after January 2023, we simply plus 5 

print(pd.Period('1/2023') + 5) # June 2023

# If we want to find out two days before March 5th 2023, we simply subtract 2

print(pd.Period('3/5/2023') - 2, "\n")

# Period object encapsulates the granularity for arithmetic.

# 'DateTimeIndex' and 'PeriodIndex'

t1 = pd.Series(list('abc'), [pd.Timestamp('2023-01-08'), pd.Timestamp('2023-01-09'), pd.Timestamp('2023-01-10')], name='t1')

print(t1)
print(type(t1))
print(type(t1.index), "\n")

t2 = pd.Series(['a', 'b', 'c'], index=[pd.Timestamp('2023-01-08'), pd.Timestamp('2023-01-09'), pd.Timestamp('2023-01-10')], name='t2')

print(t2)
print(type(t2))
print(type(t2.index), "\n")

# Similarly, we can create a period-based index as well.

t3 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])

print(t3)
print(type(t3))
print(type(t3.index), "\n")

# Converting to Datetime

# Suppose we have a list of strings and we want to create a new DataFrame

d1 = ['2 June 2023', 'Aug 29, 2023', '2023-12-09' , '7/12/23'] # date fields from multiple places 

rd = pd.DataFrame(np.random.randint(10, 100, (4, 2)), index=d1, columns=list('AB'))
# random.randint(low(inclusive), high(exclusive), size(m*n; rows*columns))
print(rd)

rd.index = pd.to_datetime(rd.index) # to_datetime convert these to Datetime and put them in a standard format
print(rd)

# to_datetime also has options to change the date parse order. For example, we can pass in the argument 'dayfirst = True' to parse the date in European date.

print(pd.to_datetime('12.30.23', dayfirst=True), "\n")

# Timedelta

# Timedeltas are differences in times -- this is not the same as a period, but conceptually similar. If we want to take the difference between September 3rd and September 1st, we get a Timedelta of two days.

print(pd.Timestamp('2/8/2023')-pd.Timestamp('10/13/2020'))
print(type(pd.Timestamp('2/8/2023')-pd.Timestamp('10/13/2020'))) # timedelta

# We can also do something like find what the date and time is for 12 days and three hours past September 2nd, at 8:10 AM.

print(pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H'), "\n")

# Offset

# Offset is similar to timedelta, but it follows specific calendar duration rules. Offset allows flexibility in terms of types of time intervals. Besides hour, day, week, month, etc. it also has business day, end of month, semi month begin, etc.

print(str(pd.Timestamp('9/4/2016').weekday()) + " September 4th")

# Now we can add the timestamp with a week ahead.

print(str(pd.Timestamp('9/4/2016') + pd.offsets.Week()) + " September 4th + a week")

# Now let's try to do the month end, then we would have the last day of September

print(str(pd.Timestamp('9/4/2016') + pd.offsets.MonthEnd()) + " Last day of the month (September) \n")

# Working with Dates in a DataFrame

# Suppose we want to look at nine measurements, taken bi-weekly, every Sunday, starting in October 2016. Using date_range, we can create this DateTimeIndex. In date_range, we have to either specify the start or end date. If it is not explicitly specified, by default, the date is considered the start date. Then we have to specify number of periods, and a frequency. 

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN') # "2W-SUN", which means biweekly on Sunday; like regex, there is sort of a mini language to describe these periods
print(dates)

print(pd.date_range('10-01-2016', periods=9, freq='B'))

print(pd.date_range('04-01-2016', periods=12, freq='QS-JUN'))

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(), 'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
print(df)
print(df.index) 
print(df.diff(), "\n") # diff to find the difference between each date's value

# Suppose we want to know what the mean count is for each month in our DataFrame. WE can do this using resample. Converting from a higher frequency from a lower frequency is called downsampling.

print(df.resample('M').mean(), "\n")

# Datetime indexing and slicing

# We can use partial string indexing to find values from a particular year or month.

print(df.loc['2017'])

print(df.loc['2016-12'])

print(df.loc['2016-12':]) # slice on a range of dates; here we only want the values from December 2016 onwards

