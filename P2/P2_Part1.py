#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:04:08 2026

@author: rebeccamonk
"""
# %% import os, np, pandas and set the working directory with the data file
import os 
import pandas as pd
os.chdir("/Users/rebeccamonk/Desktop/MNKREB002-SCDM2026/P1/") # change the working directory
# %% import the data into Spyder
filename = "ctd_profiles.dat"
ctd_data = pd.read_csv(filename, sep='\t') 
# indicate that the file is tab seperated as read_csv assumes the file is comma seperated
# %% import matplotlib and create the subplots
import matplotlib.pyplot as plt 
fig, ax = plt.subplots(1,2, sharey=True) # create small multiples with subplots - this creates 2 plots side-by-side
# %% view the data in a table for column names
print(ctd_data.head())
print(ctd_data.columns)
# %% add data to the left subplot (Temperature)
ax[0].plot(ctd_data["Temperature_degC"], ctd_data["Depth_m"], color='r')
ax[0].set_ylabel("Depth (m)")
ax[0].set_xlabel("Temperature (degC)")
ax[0].set_title("Temperature Profile")
ax[0].invert_yaxis() # since the y-axis is shared, this only needs to occur once
# %% add data to the right subplot (Salinity)
ax[1].plot(ctd_data["Salinity_PSU"], ctd_data["Depth_m"], color='b')
ax[1].set_ylabel("Depth (m)")
ax[1].set_xlabel("Salinity (PSU)")
ax[1].set_title("Salinity Profile")
# %% show the plots
plt.show() # always write this line at the end 
