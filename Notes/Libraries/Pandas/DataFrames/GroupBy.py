# Group By

# The idea behind the groupby() function is that it takes some DataFrame, splits into chunks based on some key values, applies computation on those chunks, then combines the results back together into another DataFrame. In Pandas this is referred to as the split-apply-combine pattern.

import pandas as pd
import numpy as np

df = pd.read_csv('/home/aspphem/Desktop/CSV/census.csv')
df = df[df['SUMLEV'] == 50]
print(df.head())

for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
    print('Counties in state ' + state + ' have an average population of ' + str(avg))
    
print("Approach using groupby() function\n")   
   
for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print('Counties in state ' + group + ' have an average population of ' + str(avg))
    
df = df.set_index('STNAME')

def set_batch_number(item):
    if item[0] < 'M':
        return 0
    if item[0] < 'Q':
        return 1
    return 2
    
for group, frame in df.groupby(set_batch_number):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.') 

# This time we didn't pass in a column name to groupby(). Instead, we set the index of the DataFrame to be STNAME, and if no column identifier is passed groupby() will automatically use the index.

df = pd.read_csv('/home/aspphem/Desktop/CSV/listings.csv')
print(df.head())

# So, how would we group by both of these columns ('cancellation_policy' and 'review_scores_value')? One approach might be to promote them to a multiindex and just call groupby().

df = df.set_index(['cancellation_policy', 'review_scores_value'])
print(df.head())

# When we have a multiindex we need to pass in the levels we are interested in grouping by.

for group, frame in df.groupby(level=(0,1)):
    print(group)
    
# What if we wanted to group by the cancellation policy and review scores, but separate out all the 10's from those under ten? In this case we could use a function to manage the groupings.

def grouping_fun(item): # Check the "review_scores_value" portion of the index; item is in the format of tuple (cancellation_policy, review_scores_value)
    if item[1] == 10.0:
        return (item[0], "10.0")
    else:
        return (item[0], "not 10.0")
        
for group, frame in df.groupby(by=grouping_fun):
    print(group)
    
print(df.head())

# Pandas has three broad categories of data processing to happen during the apply step. Aggregation of group data; Transformation of group data; and Filtration of group data.

# Aggregation

# The most straight forward apply step is the aggregation of data, and uses the method agg() on the groupby object. With agg() we can pass in a dictionary of the columns we are interested in aggregating along with the function we are looking to apply to aggregate.

df = df.reset_index()

print(df.groupby("cancellation_policy").agg({"review_scores_value":np.average})) # np.average doesn't ignore NaN values

print(df.groupby("cancellation_policy").agg({"review_scores_value":np.nanmean}))

# We can just extend this dictionary to aggregate by multiple functions or multiple columns.

print (df.groupby("cancellation_policy").agg({"review_scores_value":(np.nanmean,np.nanstd), "reviews_per_month":np.nanmean}))

# First we are doing a group by on the DataFrame object by the column "cancellation_policy". This creates a new grouby object. Then we are invoking the agg() function on that object. The agg function is going to apply one of more functions we specify to the group DataFrame and return a single row per DataFrame/Group. 

# When we called this function we sent it two dictionaries entries, each with the key indicating which column we wanted functions applied to. For the first column we actually supplied a tuple of two functions. Note that these are NOT function invocations, like np.nanmean(), or function names, like "nanmean". They are references to functions which will return single values. The groupby object will recognize the tuple and call each function in order on the same column; the results will be in a heirarchical index, but since they are columns they don't show as an index per se. Then we indicated another column and a single function we wanted to run.

# Transformation

# Transformation is different from aggregation. Where agg() returns a single value per column, so one row per group, transform() returns an object that is the same size as the group. Essentially, it broadcasts the function you supply over the grouped DataFrame, returning a new DataFrame. This makes combining data later easy.

# Suppose we want to include the average rating values in a given group by cancellation policy, but preserve the DataFrame shape so that we could generate a difference between an individual observation and the sum.

cols = ['cancellation_policy', 'review_scores_value'] # Subset of columns  we are interested in
transform_df = df[cols].groupby('cancellation_policy').transform(np.nanmean)
print(transform_df.head())

# We can see that the index is actually the same as the original DataFrame so lets just join this in. 

transform_df.rename({'review_scores_value': 'mean_review_scores'}, axis='columns', inplace=True)
df = df.merge(transform_df, left_index=True, right_index=True)
print(df.head()) 

df['mean_diff']=np.absolute(df['review_scores_value']-df['mean_review_scores'])
print(df['mean_diff'].head())

# Filtering

# The filter() function takes in a function which it applies to each group DataFrame and returns either a True or a False, depending upon whether that group should be included in the results.

# If we only want those groups which have a mean rating above 9 included in our results. 

print(df.groupby('cancellation_policy').filter(lambda x: np.nanmean(x['review_scores_value'])>9.3))

# Notice that the results are still indexed, but that any of the results which were in a group with a mean review score of less than or equal to 9.2 were not copied over.

# Applying

# The most common operation on groupby objects is the apply() function. This allows you to apply an arbitrary function to each group, and stitch the results back for each apply() into a single DataFrame where the index is preserved. 

df = pd.read_csv('/home/aspphem/Desktop/CSV/listings.csv')
df = df[['cancellation_policy', 'review_scores_value']]
print(df.head())

def calc_mean_review_scores(group): # group is a DataFrame just of whatever we have grouped by, e.g. cancellation policy, so we can treat this as the complete DataFrame
    avg = np.nanmean(group['review_scores_value'])
    group['review_scores_mean'] = np.abs(avg-group['review_scores_value']) # broadcast our formula and create a new column
    return group
    
print(df.groupby('cancellation_policy').apply(calc_mean_review_scores).head())


