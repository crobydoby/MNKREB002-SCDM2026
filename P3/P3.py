#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:03:00 2026

@author: rebeccamonk
"""
# %% import packages and set the working directory
import os
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

os.chdir("/Users/rebeccamonk/Desktop/MNKREB002-SCDM2026/P3/") # set the working directory
# %% The Antarctic Continent and the Southern Ocean
ccrs.SouthPolarStereo(central_longitude=0.0, true_scale_latitude=None, globe=None) # initial projection
ccrs.PlateCarree(central_longitude=0.0, globe=None) # coordinate system

plt.axes(projection=ccrs.SouthPolarStereo()) # create the axes using South Polar Stereo Projection
plt.figure() # plotting the figure 

ax = plt.axes(projection=ccrs.SouthPolarStereo()) # defining the axes
ax.coastlines() # adding the coastlines

extent = [-180, 180, -90, -60] # define the extent with the coordinate system 
ax.set_extent(extent, crs=ccrs.PlateCarree()) # set the extent with PlateCarree coordinate system

gl = ax.gridlines(draw_labels=True) # adding gridlines with labels

# Adding Features to the Map
ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN, facecolor="lightblue")

plt.title("Antarctica and the Southern Ocean")
plt.show()
# %% The South Atlantic Ocean
ccrs.EquidistantConic(central_longitude=0.0, central_latitude=-30.0, false_easting=0.0, false_northing=0.0, standard_parallels=(-20.0, -50.0), globe=None)
ccrs.PlateCarree(central_longitude=0.0, globe=None) # coordinate system

plt.figure()
plt.axes(projection=ccrs.EquidistantConic())

# Setting the Projection and the Map Extent 
ax = plt.axes(projection=ccrs.EquidistantConic(central_longitude=-10, central_latitude=-35))
extent = [-60, 30, -50, -20]
ax.set_extent(extent, crs=ccrs.PlateCarree())

# Adding Features to the Map
ax.coastlines()
ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN, facecolor="lightblue")

# Adding Gridlines and Grid Labels
gl = ax.gridlines(draw_labels=True)
gl.right_labels = True
gl.top_labels = False

# Adding the Locations
geolocator = Nominatim(user_agent='educational')
place = ['Cape Town','Walvis Bay','Rio de Janeiro','Montevideo']
address = []
for p in place:
    loc = geolocator.geocode(p,language="en")
    address.append(loc)
print(address)

# Adding City Labels Markers
for p in range(len(place)):
    ax.text(address[p].longitude, address[p].latitude,place[p], transform=ccrs.Geodetic(), rotation=0, fontsize=9, color='black')
    ax.scatter(address[p].longitude, address[p].latitude, transform=ccrs.Geodetic(), marker='o', color='black', s=10, zorder=5)

# Adding and Moving the Title
ax.set_title("Cities on the Coast of the South Atlantic Ocean", pad=50)

# Calculating the Distances
CT = geolocator.geocode('Cape Town')
MV = geolocator.geocode('Montevideo')
RJ = geolocator.geocode('Rio de Janeiro')
WB = geolocator.geocode('Walvis Bay')
print("The distance between Cape Town and Montevideo is ", geodesic(CT.point, MV.point).km," km")
print("The distance between Wavlis Bay and Rio de Janeiro is ", geodesic(WB.point, RJ.point).km," km")

# Adding Great Circles
longitude1 = CT.longitude, MV.longitude
latitude1 = CT.latitude, MV.latitude
ax.plot(longitude1, latitude1, transform=ccrs.Geodetic(), label='6686 km', color='green')

longitude2 = RJ.longitude, WB.longitude
latitude2 = RJ.latitude, WB.latitude
ax.plot(longitude2, latitude2, transform=ccrs.Geodetic(), label='5879 km', color='red')

plt.legend(fontsize='small', loc="lower left")
# %% False Bay Resolution Maps
ccrs.PlateCarree(central_longitude=0.0, globe=None)

# Setting the Map Extent 
extent = [18, 19, -34.5, -34]

# Creating the Coastline Resolutions
resolutions = ['110m', '50m', '10m']
titles = ["Coarse Resolution (110 m)", "Intermediate Resolution (50 m)", "Full Resolution (10 m)"]

# Creating the Figure with Subplots
fig, axes = plt.subplots(1, 3, figsize=(10,6), subplot_kw={'projection':ccrs.PlateCarree()}, constrained_layout=True)

# Setting the Extent, Adding the Coastlines, Feature and Gridlines with Titles
for i, ax in enumerate(axes):
    ax.set_extent(extent, crs=ccrs.PlateCarree())
    ax.coastlines(resolution=resolutions[i])
    gl = ax.gridlines(draw_labels=True, color="gray")
    gl.top_labels = False
    gl.right_labels = False
        
    ax.set_title(titles[i])
    
    # Overlaying the Land and Ocean Features
    ax.add_feature(cartopy.feature.LAND)
    ax.add_feature(cartopy.feature.OCEAN, facecolor="lightblue")
    
# Adding a Figure Title and Axis Labels
fig.suptitle("False Bay Coastline Shown In Different Resolutions", y=0.7)
fig.supxlabel("Longitude (ºE)", y=0.3)
fig.supylabel("Latitude (ºS)")

plt.show()



    







