import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

###################################################################################################################

def wrangle_sa_temp():
    
    df = pd.read_csv('GlobalLandTemperaturesByCity.csv')
    
    ## Only looking for observations in city of San Antonio, TX
    san_antonio = df[df['City'] == 'San Antonio']
    
    # Reassign the sale_date column to be a datetime type
    san_antonio.dt = pd.to_datetime(san_antonio.dt)
    
    # Sort rows by the date and then set the index as that date
    san_antonio = san_antonio.set_index("dt").sort_index()
    
    # Create month and year columns
    san_antonio['month'] = san_antonio.index.month
    san_antonio['year'] = san_antonio.index.year
    
    ## observations prior to 1823 will be removed for missing values 
    san_antonio = san_antonio[san_antonio['year'] > 1822]
    
    # Remove unnecesary columns
    san_antonio = san_antonio.drop(columns = ['City', 'Country', 'Latitude', 'Longitude'])
    
    return san_antonio

###################################################################################################################

