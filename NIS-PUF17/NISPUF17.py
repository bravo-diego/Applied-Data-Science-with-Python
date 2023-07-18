# For this assignment you'll be looking at 2017 data on immunizations from the CDC. Your datafile for this assignment is in assets/NISPUF17.csv. A data users guide for this, which you'll need to map the variables in the data to the questions being asked, is available at assets/NIS-PUF17-DUG.pdf.

# PART A -- Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college graduate.

# This function should return a dictionary in the form of (use the correct numbers, do not round numbers).

    # Loading libraries

import pandas as pd 
import numpy as np
import scipy.stats as stats

def proportion_of_education():
    df = pd.read_csv("/home/aspphem/Desktop/CSV/NISPUF17.csv")
    s = df['EDUC1'].value_counts() # .value_counts() method; Series.dtype
    dic = {'less than high school': s.iloc[3]/len(df.iloc[:,23]), 'high school': s.iloc[2]/len(df.iloc[:,23]), 'more than high school but not college': s.iloc[1]/len(df.iloc[:,23]), 'college': s.iloc[0]/len(df.iloc[:,23])}
    return dic
    
# .value_counts() method count the number of occurrences in a column in a dataframe. If you type df['condition'].value_counts() you will get the FREQUENCY OF EACH UNIQUE VALUE in the column 'condition'.

# PART B -- Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.

# This function should return a tuple in the form (2.1, 0.1).
 
def average_influenza_doses():
    df = pd.read_csv("/home/aspphem/Desktop/CSV/NISPUF17.csv")
    columns = ['CBF_01', 'P_NUMFLU']
    updated_df = df[columns]
    # Children who received breastmilk
    breastmilk_mask = updated_df['CBF_01'] == 1
    yes_df = updated_df.where(breastmilk_mask).dropna()
    x = yes_df.mean(axis = 0) # Average number of vaccines for children who received breastmilk
    # Children who didn't received breastmilk
    no_breastmilk_mask = updated_df['CBF_01'] == 2
    no_df = updated_df.where(no_breastmilk_mask).dropna()
    y = no_df.mean(axis = 0) # Average number of vaccines for children who didn't received breastmilk
    t = (x.iloc[1], y.iloc[1])
    return t

# PART C -- It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child. Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.

# This function should return a dictionary:

#{"male": 0.0099, "female": 0.0077}

def chickenpox_by_sex():
    df = pd.read_csv("/home/aspphem/Desktop/CSV/NISPUF17.csv")
    updated_df = df[['SEX', 'HAD_CPOX', 'P_NUMVRC']]
    M = updated_df[(updated_df['SEX'] == 1) & (updated_df['P_NUMVRC'] > 0)] # Male
    IM = M['HAD_CPOX'].value_counts() # Number of infected children
    x = IM.iloc[1]/IM.iloc[0] # Ratio Males
    F = updated_df[(updated_df['SEX'] == 2) & (updated_df['P_NUMVRC'] > 0)] # Female
    IF = F['HAD_CPOX'].value_counts() # Number of infected children
    y = IF.iloc[1]/IF.iloc[0] # Ratio Females
    dic = {'male': x, 'female': y}
    return dic

# PART D -- A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the correlation between the use of the vaccine and whether it results in prevention of the infection or disease. In this question, you are to see if there is a correlation between having had chicken pox and the number of chickenpox vaccine doses given (varicella).

# The had_chickenpox_column is either 1 (for yes) or 2 (for no), and the num_chickenpox_vaccine_column is the number of doses a child has been given of the varicella vaccine. A positive correlation (e.g., corr > 0) means that an increase in had_chickenpox_column (which means more no's) would also increase the values of num_chickenpox_vaccine_column (which means more doses of vaccine). If there is a negative correlation (e.g., corr < 0), it indicates that had chickenpox is related to an increase in the number of vaccine doses.

# Also, pval is the probability that we observe a correlation between had_chickenpox_column and num_chickenpox_vaccine_column which is greater than or equal to a particular value occurred by chance. A small pval means that the observed correlation is highly unlikely to occur by chance. In this case, pval should be very small (will end in e-18 indicating a very small number).

def corr_chickenpox():
    df = pd.read_csv("/home/aspphem/Desktop/CSV/NISPUF17.csv")
    updated_df = df[['HAD_CPOX', 'P_NUMVRC']]
    filtered_df = updated_df[updated_df['HAD_CPOX'] <= 2]
    new_df = filtered_df[~filtered_df['P_NUMVRC'].isna() & ~filtered_df['HAD_CPOX'].isna()]
    corr, pval=stats.pearsonr(new_df['HAD_CPOX'], new_df['P_NUMVRC'])
    return corr


