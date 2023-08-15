# Mapping and Geographic Investigation -- Geographical Information Systems

import folium
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.rcParams['figure.figsize'] = [16.0, 8.0] # figure size will be the same throughout our investigation 

df = pd.read_csv("/home/aspphem/Desktop/CSV/wipeout.csv")
print(df.head()) 

df['position_lat_degrees'] = df['position_lat'] * (180 / 2**31)
df['position_long_degrees'] = df['position_long'] * (180 / 2**31)

def lat2y(a):
    return 180.0/math.pi*math.log(math.tan(math.pi/4.0+a*(math.pi/180.0)/2.0))

df['position_lat_degrees_mercantor'] = df['position_lat_degrees'].apply(lat2y)

df = df[['timestamp', 'enhanced_altitude', 'enhanced_speed', 'heart_rate', 'position_lat_degrees_mercantor', 'position_long_degrees', 'position_lat_degrees']].dropna() # drop missing values
print(df.head())

image = plt.imread("/home/aspphem/Desktop/PNG/map.png") # image from Open Street Map
plt.imshow(image, alpha=0.5, extent=[-83.77141, -83.75977, 46.75230, 46.76620]) 
# alpha - transparency of image; extent - bounds of the map, using the same coordinate system as the axis object itself

small_df = df[(df['position_long_degrees'] > -83.77141) & (df['position_long_degrees'] < -83.75977) & (df['position_lat_degrees_mercantor'] > 46.75230) & (df['position_lat_degrees_mercantor'] < 46.76620)] # slicing data frame between latitude and longitude values

plt.scatter(small_df['position_long_degrees'], small_df['position_lat_degrees_mercantor'], s=10, c=small_df['heart_rate'], cmap='Blues', alpha=0.75) # s - size of point; c - color changing based on Heart Rate column; cmap - color itself; alpha - transparency of image

plt.colorbar().set_label('Heart Rate (bpm)') # adding a color bar
plt.suptitle('Heart Rate data from {} to {}'.format(np.min(small_df['timestamp']),np.max(small_df['timestamp'])), size='10') # setting title
plt.show()

# Same map using all of the data points in it

plt.imshow(image, alpha=0.5, extent=[-83.77141, -83.75977, 46.75230, 46.76620]) 

plt.scatter(df['position_long_degrees'], df['position_lat_degrees_mercantor'], s=10, c=df['heart_rate'], cmap='Blues', alpha=0.75)

plt.colorbar().set_label('Heart Rate (bpm)')

plt.suptitle('Heart Rate data from {} to {}'.format(np.min(small_df['timestamp']),np.max(small_df['timestamp'])), size='10')

plt.show()

# Tile Server -- tile servers create a matrix of maps different zoom levels and the they serve up portions of the map

m = folium.Map(location=[42.24, -83.764], zoom_start=12)

folium.Marker([df['position_lat_degrees'].iloc[0], df['position_long_degrees'].iloc[0]], popup='Start').add_to(m)

folium.Marker([df['position_lat_degrees'].iloc[-1], df['position_long_degrees'].iloc[-1]], popup='Stop').add_to(m)

route = folium.PolyLine(locations=zip(df['position_lat_degrees'], df['position_long_degrees']), weight=5, color='blue').add_to(m) # map the whole cycling route; PolyLine takes a list of locations as tuples, which means we have to combine our latitude and longitude values pairwise and this is easily achieved through the use of python's zip() function

m.save('index.html')


