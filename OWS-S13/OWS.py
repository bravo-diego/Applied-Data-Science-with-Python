# Overwatch 2 Overbuff Statistics - How Trends in Heroes Changes Between Seasons and Skill Tiers? 

    # Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.reset_option("display")

    # Loading Data Sets

# Hero Statistics Season 1
season_one = pd.read_csv("/home/aspphem/Desktop/Overwatch/OW2_S1.csv") 
# Hero Statistics Season 2
season_two = pd.read_csv("/home/aspphem/Desktop/Overwatch/OW2_S2.csv") 
# Hero Statistics Season 3
season_three = pd.read_csv("/home/aspphem/Desktop/Overwatch/OW2_S3.csv")

    # Describing Data

print(season_one.head(3), "Season One Data Frame has {} rows and {} columns.".format(season_one.shape[0], season_one.shape[1])) # season one data frame preview and shape, (280 rows, 132 columns)
print(season_one.keys())
print(season_one.describe(include=[object])[['Hero', 'Skill Tier', 'Role']]) # statistics of no-numerical features

print("Season Two Data Frame has {} rows and {} columns.".format(season_two.shape[0], season_two.shape[1])) 
print(season_two.describe(include=[object])[['Hero', 'Skill Tier', 'Role']]) # statistics of no-numerical features
print("Season Three Data Frame has {} rows and {} columns.".format(season_three.shape[0], season_three.shape[1])) # season two and season three data frames shape, (288 rows, 135 columns); Sigma was added in season two

    # Data Cleaning
        
        # Relevant Data Frames Seasons 1 to 3 

columns = [0,1,2,3,4,5,6,7,8,9,10,-1] # relevant columns; we are not interested in specific statistics about every hero 

season_one_relevant_data =  season_one.iloc[:, columns] # season one relevant data

print(season_one_relevant_data.head(10), season_one_relevant_data.shape) # shape (288 rows, 12 columns)

season_one_updated_data = season_one_relevant_data[season_one_relevant_data['Skill Tier'] != 'All'].rename(columns={'KDA Ratio': 'KDA', 'Pick Rate, %': 'Pick Rate', 'Win Rate, %': 'Win Rate'})
print(season_one_updated_data.head(10), season_one_updated_data.shape)
print(season_one_updated_data.keys())

season_two_relevant_data =  season_two.iloc[:, columns] # season two relevant data
season_two_updated_data = season_two_relevant_data[season_two_relevant_data['Skill Tier'] != 'All'].rename(columns={'KDA Ratio': 'KDA', 'Pick Rate, %': 'Pick Rate', 'Win Rate, %': 'Win Rate'})
print(season_two_updated_data.head(3), season_two_updated_data.shape)

season_three_relevant_data =  season_three.iloc[:, columns] # season three relevant Data
season_three_updated_data = season_three_relevant_data[season_three_relevant_data['Skill Tier'] != 'All'].rename(columns={'KDA Ratio': 'KDA', 'Pick Rate, %': 'Pick Rate', 'Win Rate, %': 'Win Rate'})
print(season_three_updated_data.head(3), season_three_updated_data.shape)

        # All Seasons Data Frame

season_one_updated_data_copy = season_one_updated_data.copy() # create a copy
season_one_updated_data_copy['Season'] = 1 # season column to identify (classify) points of data 

season_two_updated_data_copy = season_two_updated_data.copy()
season_two_updated_data_copy['Season'] = 2 

season_three_updated_data_copy = season_three_updated_data.copy() 
season_three_updated_data_copy['Season'] = 3 

all_seasons_relevant_data = pd.merge(pd.merge(season_one_updated_data_copy, season_two_updated_data_copy, how='outer'), season_three_updated_data_copy, how='outer')

all_seasons_relevant_data = all_seasons_relevant_data.loc[:, ['Season', 'Hero', 'Skill Tier', 'Pick Rate', 'Win Rate']]
print(all_seasons_relevant_data)
print("There are {} different seasons, {} different heroes and {} different skill tiers.".format(all_seasons_relevant_data['Season'].nunique(), all_seasons_relevant_data['Hero'].nunique(), all_seasons_relevant_data['Skill Tier'].nunique()))

    # Visualizing Data

        # Heroes and their Average Pick Rates per Season
        
season_one_pick_rate = season_one_updated_data.groupby(["Hero"]).agg({"Pick Rate":np.nanmean}).reset_index() 
season_two_pick_rate = season_two_updated_data.groupby(["Hero"]).agg({"Pick Rate":np.nanmean}).reset_index()
season_three_pick_rate = season_three_updated_data.groupby(["Hero"]).agg({"Pick Rate":np.nanmean}).reset_index()

        # Chart Season One

        # Customize Bar Colors
        
min_pick_rate_one = min(season_one_pick_rate['Pick Rate'])

bar_colors = []
for value in season_one_pick_rate['Pick Rate']:
    if value == min_pick_rate_one:
        bar_colors.append('indianred')
    elif value < 3.5:
        bar_colors.append('lightgray')
    else:
        bar_colors.append('lightcoral')
        
        # Change General Chart Options
        
plt.figure(figsize=(13,8)) # figure size
plt.suptitle('How have been changing heroes and team composition between seasons in Overwatch 2?', fontsize=14) # main title

ax1 = plt.subplot(2,3,1) # (2 rows, 3 columns; index 1)
plt.bar(season_one_pick_rate['Hero'], season_one_pick_rate['Pick Rate'], color = bar_colors)

plt.title('Season 1')
plt.ylabel('Average Pick Rate')
plt.xlabel('Hero')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.xticks([])
plt.yticks([])

        # Modify Chart Labels 

x = plt.gca()
for item in x.get_xticklabels():
    item.set_rotation(90) 

def labels(x, y):
    c = 0
    for i in range(len(x)):
        if y[i] > 3.5:
            s = "{} - {:.3}%"
            plt.text(i, y[i]+0.5, s.format(x[i], y[i]), ha = 'center', alpha = 0.75, fontsize = 'x-small', rotation = 'vertical') # text(x, y, s, parameters); x and y -- float values, position to place the text, coordinates; s -- text; ha -- horizontal alignment 
        elif y[i] == min_pick_rate_one:
            s = "{} - {:.3}%"
            plt.text(i, y[i]+0.5, s.format(x[i], y[i]), ha = 'center', alpha = 0.75, fontsize = 'x-small', rotation = 'vertical')
        else:
            c += 1
            
labels(season_one_pick_rate['Hero'], season_one_pick_rate['Pick Rate'])

        # Chart Season 2

        # Customize Bar Colors
        
min_pick_rate_two = min(season_two_pick_rate['Pick Rate'])

bar_colors2 = []
for value in season_two_pick_rate['Pick Rate']:
    if value == min_pick_rate_two:
        bar_colors2.append('indianred')
    elif value < 3.5:
        bar_colors2.append('lightgray')
    else:
        bar_colors2.append('lightcoral')
        
        # Change General Chart Options
        
ax2 = plt.subplot(2,3,2, sharey=ax1, sharex=ax1) # (2 rows, 3 columns; index 2)
plt.bar(season_two_pick_rate['Hero'], season_two_pick_rate['Pick Rate'], color = bar_colors2)

plt.title('Season 2')
plt.xlabel('Hero')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

plt.xticks([])
plt.yticks([])

        # Modify Chart Labels 

x = plt.gca()
for item in x.get_xticklabels():
    item.set_rotation(90) 

def labels(x, y):
    c = 0
    for i in range(len(x)):
        if y[i] > 3.5:
            s = "{} - {:.3}%"
            plt.text(i, y[i]+0.5, s.format(x[i], y[i]), ha = 'center', alpha = 0.75, fontsize = 'x-small', rotation = 'vertical') # text(x, y, s, parameters); x and y -- float values, position to place the text, coordinates; s -- text; ha -- horizontal alignment 
        elif y[i] == min_pick_rate_two:
            s = "{} - {:.3}%"
            plt.text(i, y[i]+0.5, s.format(x[i], y[i]), ha = 'center', alpha = 0.75, fontsize = 'x-small', rotation = 'vertical')
        else:
            c += 1
            
labels(season_two_pick_rate['Hero'], season_two_pick_rate['Pick Rate'])

        # Chart Season 3

        # Customize Bar Colors
        
min_pick_rate_three = min(season_three_pick_rate['Pick Rate'])

bar_colors3 = []
for value in season_three_pick_rate['Pick Rate']:
    if value == min_pick_rate_three:
        bar_colors3.append('indianred')
    elif value < 3.5:
        bar_colors3.append('lightgray')
    else:
        bar_colors3.append('lightcoral')
        
        # Change General Chart Options
        
ax2 = plt.subplot(2,3,3, sharey=ax1, sharex=ax1) # (2 rows, 3 columns; index 3)
plt.bar(season_three_pick_rate['Hero'], season_three_pick_rate['Pick Rate'], color = bar_colors3)

plt.title('Season 3')
plt.xlabel('Hero')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

plt.xticks([])
plt.yticks([])

        # Modify Chart Labels 

x = plt.gca()
for item in x.get_xticklabels():
    item.set_rotation(90) 

def labels(x, y):
    c = 0
    for i in range(len(x)):
        if y[i] > 3.5:
            s = "{} - {:.3}%"
            plt.text(i, y[i]+0.5, s.format(x[i], y[i]), ha = 'center', alpha = 0.75, fontsize = 'x-small', rotation = 'vertical') # text(x, y, s, parameters); x and y -- float values, position to place the text, coordinates; s -- text; ha -- horizontal alignment 
        elif y[i] == min_pick_rate_three:
            s = "{} - {:.3}%"
            plt.text(i, y[i]+0.5, s.format(x[i], y[i]), ha = 'center', alpha = 0.75, fontsize = 'x-small', rotation = 'vertical')
        else:
            c += 1
            
labels(season_three_pick_rate['Hero'], season_three_pick_rate['Pick Rate'])

        # Relationship Between Pick Rate and Win Rate
        
ax3 = plt.subplot(2,2,3)

plt.scatter(x = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Bronze']['Pick Rate'], y = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Bronze']['Win Rate'], c = 'indianred', label = 'Bronze', alpha = 0.85)

plt.scatter(x = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Silver']['Pick Rate'], y = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Silver']['Win Rate'], c = 'silver', label = 'Silver', alpha = 0.80)

plt.scatter(x = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Gold']['Pick Rate'], y = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Gold']['Win Rate'], c = 'palegoldenrod', label = 'Gold', alpha = 0.75)

plt.scatter(x = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Platinum']['Pick Rate'], y = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Platinum']['Win Rate'], c = 'slategrey', label = 'Platinum', alpha = 0.70)

        # Draw a Trendline

x = all_seasons_relevant_data[(all_seasons_relevant_data['Pick Rate'] != 'Diamond') & (all_seasons_relevant_data['Pick Rate'] != 'Master') & (all_seasons_relevant_data['Pick Rate'] != 'Grandmaster')]['Pick Rate']
y = all_seasons_relevant_data[(all_seasons_relevant_data['Pick Rate'] != 'Diamond') & (all_seasons_relevant_data['Pick Rate'] != 'Master') & (all_seasons_relevant_data['Pick Rate'] != 'Grandmaster')]['Win Rate']

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), '--', lw=1, color='dimgrey')

        # Change General Chart Options

plt.title('Lowest Skill Tiers')
plt.xlabel('Pick Rate')
plt.ylabel('Win Rate')
plt.legend(bbox_to_anchor=(0.85, 0.36), ncol=2, loc=9, fancybox=True, shadow=True)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

ax4 = plt.subplot(2,2,4, sharey=ax3, sharex=ax3)
plt.scatter(x = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Diamond']['Pick Rate'], y = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Diamond']['Win Rate'], c = 'darkturquoise', label = 'Diamond', alpha = 0.85)

plt.scatter(x = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Master']['Pick Rate'], y = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Master']['Win Rate'], c = 'khaki', label = 'Master', alpha = 0.75)

plt.scatter(x = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Grandmaster']['Pick Rate'], y = all_seasons_relevant_data[all_seasons_relevant_data['Skill Tier'] == 'Grandmaster']['Win Rate'], c = 'gold', label = 'Grandmaster', alpha = 0.70)

        # Draw a Trendline

x = all_seasons_relevant_data[(all_seasons_relevant_data['Pick Rate'] != 'Bronze') & (all_seasons_relevant_data['Pick Rate'] != 'Silver') & (all_seasons_relevant_data['Pick Rate'] != 'Gold') & (all_seasons_relevant_data['Pick Rate'] != 'Platinum')]['Pick Rate']
y = all_seasons_relevant_data[(all_seasons_relevant_data['Pick Rate'] != 'Bronze') & (all_seasons_relevant_data['Pick Rate'] != 'Silver') & (all_seasons_relevant_data['Pick Rate'] != 'Gold') & (all_seasons_relevant_data['Pick Rate'] != 'Platinum')]['Win Rate']

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "--", lw=1, color='dimgrey')

        # Change General Chart Options

plt.title('Highest Skill Tiers')
plt.xlabel('Pick Rate')
plt.legend(bbox_to_anchor=(1, 0.40), loc=9, fancybox=True, shadow=True)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.show()

# We can see how the metagame (i.e which heroes are generally considered stronger) was changing between seasons, since its release to its third season (six month later). In season one there were few heroes considered in the metagame by players, then in season two the pick rates went down for all heroes, specially support heroes. Finally in season three (current season) we can see that there are more damage heroes included in the metagame and the "weakest" hero (i.e the hero with the lowest pick rate) shows a higher pick rate compared with the others forgotten heroes in past seasons. So there is a gradual upgrade and balance between seasons so that the players can used any heroe and have chances to win the game. About the relationship between pick rate and win rate; we see that this relationship keeps more in highest skill tiers, so in those skill tiers players tend to use heroes included in the metagame.

# Data source available in Kaggle: https://www.kaggle.com/datasets/mykhailokachan/overwatch-2-statistics

# Overbuff web site: https://www.overbuff.com/

