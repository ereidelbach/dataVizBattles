#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:12:05 2018

@author: ejreidelbach
"""

#------------------------------------------------------------------------------
# Scrape the January 2018 DataIsBeautiful DataViz Battle Data set
#------------------------------------------------------------------------------

# Import the Required Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

###############################################################################
# Function Definitions

def site_to_soup(url):
    headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content,'html.parser')   
    return soup

###############################################################################
# Working Code
    
# Set the project working directory
os.chdir('/home/ejreidelbach/projects/dataVizBattles/01-2018')
    
# Scrape the monthly data site
soup = site_to_soup('http://aquatext.com/tables/algaegrwth.htm')
soupTable = soup.find_all('table')[1]

'''
    The table is going to require some "tidy-ing" up in order to make it fit
    the concept of one observation per row, one variable per column. Let's start
    making that happen by extracting the data from our soupified-html.
'''

# Extract all the rows within the data table
soupTableRows = soupTable.find_all('tr')

# Iterate through each row and extract the data contained within
tableList = []
for row in soupTableRows:
    columnsInRow = row.find_all('td')
    rowList = []
    for col in columnsInRow:
        rowList.append(col.text)
    if len(rowList) > 1:
        tableList.append(rowList)
        
# Now that we have all the data, let's start merging it into a dataframe
tempList = [5, 5, 10, 10, 25, 25, 30, 30]
luxList = [5000, 2500, 5000, 2500, 5000, 2500, 5000, 2500]
observationList = []
for algae in tableList[2:]:
    type = algae[0]
    for growth, temp, lux in zip(algae[1:], tempList, luxList):
        observationList.append([type, temp, lux, growth])
janDF = pd.DataFrame.from_records(observationList, columns = [
        'Algae','Temperature','Lux','Growth'])

# The 'growth' column is not numeric due to one value which has two decimals
#   Offender:  Isochrysis aff. galbana, 10 degrees, 5000 lux, value = 0..06
#   Index = 82 ----> Change growth to correctly be 0.06
janDF.at[82, 'Growth'] = 0.06
    
# Convert 'growth' column to numeric
janDF['Growth'] = janDF['Growth'].apply(pd.to_numeric)

# Output dataset to csv
janDF.to_csv('janData.csv', index=False)

'''
    The data is now tidy and ready for analysis.
    Time to move on to visualizing the data.
'''       
    