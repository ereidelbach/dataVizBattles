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

###############################################################################
# Function Definitions

def site_to_soup(url):
    headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content,'html.parser')   
    return soup

###############################################################################
# Working Code
    
