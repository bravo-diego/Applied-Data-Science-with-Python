import matplotlib.pyplot as plt
import numpy as np

languages = ["Python", "SQL", "Java", "C++", "Javascript"]
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

plt.figure(figsize=(10,8))
plt.bar(pos, popularity, align='center')
plt.xticks(pos, languages)
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math and Data \nby % Popularity on Stack Overflow')

for spine in plt.gca().spines.values(): # get current axis; get splines for the axis object (both x and y axis); go through the splines and set the values there to False
    spine.set_visible(False)

plt.show()

plt.figure(figsize=(10,8))
languages = ["Python", "SQL", "Java", "C++", "Javascript"]
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]


bars = plt.bar(pos, popularity, align='center', linewidth=0, color='lightslategrey') 
# change all bars color  
bars[0].set_color('#1F77B4') # change the first bar color; contrast with the others bars

plt.xticks(pos, languages, alpha = 0.8) # alpha controls the transparency
plt.yticks([]) # we can remove the y label by just setting it to an empty list
plt.title('Top 5 Languages for Math and Data \nby % Popularity on Stack Overflow', alpha = 0.8)

for spine in plt.gca().spines.values():
    spine.set_visible(False)
    
for bar in bars:
    height = bar.get_height()
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(height)) + '%', ha='center', color='w', fontsize = 11)
    
plt.show()
