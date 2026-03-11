#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:52:24 2026

@author: rebeccamonk
# %%
"""
# %% import os, np and pandas and set the working directory
import os
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
os.chdir("/Users/rebeccamonk/Desktop/MNKREB002-SCDM2026/P2/") # set the working directory
# %% import the data into Spyder and set the column for the time index
filename = "SAA2_WC_2017_metocean_10min_avg.csv"
ocean_data = pd.read_csv(filename, sep=",", parse_dates=["TIME_SERVER"], index_col=["TIME_SERVER"])
# %% check the ocean_data DataFrame
print(ocean_data.head())
print(ocean_data.columns)
# %% create a data subset from departure to 4 July
ocean_data_subset = ocean_data.loc[:"2017-07-04"]
print(ocean_data_subset)
# %% temperature timeseries with grayscale style
fig, ax = plt.subplots()
plt.style.use("grayscale")
ax.plot(ocean_data_subset.index, ocean_data_subset["TSG_TEMP"])
plt.xticks(rotation=90)
ax.set_xlabel("Time (Date)")
ax.set_ylabel("Temperature (degC)")
plt.grid(False)
plt.show()
# %% salinity distribution histogram
fig, ax = plt.subplots()
ax.hist(ocean_data_subset["TSG_SALINITY"], bins=np.arange(30, 35, 0.5))
ax.set_xlabel("Salinity (PSU)")
ax.set_ylabel("Number of Measurements")
plt.show()
# %% calculating mean, standard deviation and IQR
Tmean = ocean_data_subset["TSG_TEMP"].mean()
Tstd = ocean_data_subset["TSG_TEMP"].std()
T25 = ocean_data_subset["TSG_TEMP"].quantile(0.25)
T75 = ocean_data_subset["TSG_TEMP"].quantile(0.75)
TIQR = T75 - T25

Smean = ocean_data_subset["TSG_SALINITY"].mean()
Sstd = ocean_data_subset["TSG_SALINITY"].std()
S25 = ocean_data_subset["TSG_SALINITY"].quantile(0.25)
S75 = ocean_data_subset["TSG_SALINITY"].quantile(0.75)
SIQR = S75 - S25
# %% show the calculated values in a table
TS_stats = pd.DataFrame({
    "Mean":[Tmean, Smean],
    "Standard Deviation":[Tstd, Sstd], 
    "IQR":[TIQR, SIQR]
    }, index=["Temperature (degC)", "Salinity (PSU)"])
print(TS_stats)
# %% use the function given
def ddmm2dd(ddmm):   
    """     
    Converts a position input from degrees and minutes to degrees and decimals     
    Input is ddmm.cccc and output is dd.cccc     
    Note, it does not check if positive or negative     
    """       
    thedeg = np.floor(ddmm/100.)     
    themin = (ddmm-thedeg*100.)/60.   
    return thedeg+themin
# %% scatter plot of wind speed and air temperature
fig, ax = plt.subplots()
ax.scatter(ocean_data_subset["WIND_SPEED_TRUE"], ocean_data_subset["AIR_TEMPERATURE"], c=ocean_data_subset["LATITUDE"], cmap="viridis")
plt.grid(False)
ax.set_xlabel("Wind Speed (m/s)")
ax.set_ylabel("Air Temperature (degC)")
plt.show()
fig.savefig("windspeed_airtemp.png", dpi=300)














