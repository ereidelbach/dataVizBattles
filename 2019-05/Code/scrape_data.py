#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 4 15:16:59 2019

@author: ejreidelbach

:DESCRIPTION: This script imports URLs for reddit comments via a text file
    (pastebin_dump.txt sourced from https://pastebin.com/raw/djbR067n) and then
    proceeds to scrape each comment, storing the results in a csv (comments.csv).

:REQUIRES:
    Refer to the Package Import section of the script

:TODO:
    TBD
"""

#==============================================================================
# Package Import
#==============================================================================
import os
import pandas as pd
import pathlib
import tqdm

#==============================================================================
# Reference Variable Declaration
#==============================================================================

#==============================================================================
# Function Definitions
#==============================================================================
def function_name(var1, var2):
    '''
    Purpose: Stuff goes here

    Inputs
    ------
        var1 : type
            description
        var2 : type
            description

    Outputs
    -------
        var1 : type
            description
        var2 : type
            description
    '''
#==============================================================================
# Working Code
#==============================================================================

# Set the project working directory
path_dir = pathlib.Path('/home/ejreidelbach/Projects/dataVizBattles/2019-04/')
os.chdir(path_dir)

# Import the text file containing the comment URLs
list_comments = open('Data/pastebin_dump.txt', 'r').read().split()
