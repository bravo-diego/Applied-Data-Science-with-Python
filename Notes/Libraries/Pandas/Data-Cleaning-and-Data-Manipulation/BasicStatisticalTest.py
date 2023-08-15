# Basic Statistical Testing

# Hypothesis testing -- determine if, for instance, the two different conditions we have in an experiment have resulted in different impacts.

# When we do hypothesis testing, we actually have two statements of interest: the first is our actual explanation, which we call the alternative hypothesis, and the second is that the explanation we have is not sufficient, and we call this the null hypothesis. Our actual testing method is to determine whether the null hyphotesis is true or not. If we find that there is a difference between groups, then we can reject the null hypothesis ans we accept our alternative.

import numpy as np
import pandas as pd

from scipy import stats

df = pd.read_csv("/home/aspphem/Desktop/CSV/grades.csv")
print(df.head())
print(df.keys())
print("There are {} rows and {} columns".format(df.shape[0], df.shape[1]))

# Early finishers -- those who finish the first assignment by the end of December 2015

early_finishers = df[pd.to_datetime(df['assignment1_submission']) < '2016']
print(early_finishers.head())

# Late finishers -- those who finish it sometime after that

late_finishers = df[~df.index.isin(early_finishers.index)] # tilde sing (~) inverts boolean mask -False to True and -True to False
print(late_finishers.head())

# If we call the mean() function directly on the data frame, we see that each of the means for the assignments are calculated. 

print(early_finishers['assignment1_grade'].mean())
print(late_finishers['assignment1_grade'].mean())

# They look pretty similar. This is where the students' t test comes in. It allows us to form the alternative hypothesis ("These are different") as well as the null hypothesis ("These are the same") and then test that null hypothesis.

# When doing hypothesis testing, we have to choose a significance level as a threshold for how much of a chance we are willing to accept. This significance level is typically called alpha. For this example, let's use a threshold of 0.05 for our alpha (5%). 

# The SciPy library contains a number of different statistical tests and forms a basis for hypothesis testing in Python and we are going to use the ttest_ind() function which does an independent t-test (meaning the populations are not related to one another). The result are the t-statistic and a p-value. It's this later value the probability, which is most important to us, as it indicates the chance (between 0 and 1) of our null hypothesis being True.

from scipy.stats import ttest_ind

print(ttest_ind(early_finishers['assignment1_grade'], late_finishers['assignment1_grade']))

# Probability = 0.18 -- this means that we cannot reject the null hypothesis (null hypothesis -- two populations are the same), and we don't have enough certainty in our evidence (because it is greater than alpha) to come to a conclusion to the contrary. This doesn't mean that we have proven the populations are the same.

print(ttest_ind(early_finishers['assignment2_grade'], late_finishers['assignment2_grade']))

print(ttest_ind(early_finishers['assignment3_grade'], late_finishers['assignment3_grade']))

print(ttest_ind(early_finishers['assignment4_grade'], late_finishers['assignment4_grade']))

print(ttest_ind(early_finishers['assignment5_grade'], late_finishers['assignment5_grade']))

print(ttest_ind(early_finishers['assignment6_grade'], late_finishers['assignment6_grade']))

# It looks like in this data we do not have enough evidence to suggest the populations differ with respect to grade. 

# Assignment 3 has a p-value around 0.1. This means that if we accepted a level of chance similarity of 11% this would have been considered statistically significant. 

# P-values have come under fire recently for being insuficient for telling us enough about the interactions which are happening, and two other techniques, confidence intervals and bayesian analyses, are being used more regularly. One issue with p-values is that you run more tests you are likely to get a value which is statistically significant just by chance.

df1 = pd.DataFrame([np.random.random(100) for x in range(100)])
df2 = pd.DataFrame([np.random.random(100) for x in range(100)])

# For a given row inside of df1, is it the same as the row inside df2? Let's say our critical value is 0.1 or and alpha of 10%. And we are going to compare each column in df1 to the same numbered column in df2. And we'll report when the p-value isn't less than 10%, which means that we have sufficient evidence to say that the columns are different.

def test_column(alpha=0.1):
    num_diff=0
    for col in df1.columns:
        teststat,pval=ttest_ind(df1[col],df2[col])
        if pval <= alpha: 
            print("Col {} is statistically significantly different at alpha={}, pval{}".format(col,alpha,pval))
            num_diff=num_diff+1
    print("Total number different was {}, which is {}%".format(num_diff, float(num_diff)/len(df1.columns)*100))
    
print(test_column(alpha=0.1))
print(test_column(alpha=0.05))

# So we see that there are a bunch of columns that are different. In fact, the number looks a lot like the alpha value we choose. So what's going on - shouldn't all of the columns be the same? Remember that all the ttest does is check if tow sets are similar given some level of confidence, in our case 10%. The more random comparisons you do, the moer will just happen to be the same by chance. In this example we checked 100 columns, so we could expect there to be roughly 10 of them if our alpha was 0.1

# Significance -- means the evidence we observed from the data against the null hypothesis, and alpha level is a measure or our tolerance of the significance.

# The p value reports the probability we can get the observed data under the null hypothesis, so with a larger p value (by larger we mean it is closer to 1, instead of saying that is more extreme), we have less evidence to reject the null hypothesis. With a large alpha, we reject the null hypothesis less carefully.
