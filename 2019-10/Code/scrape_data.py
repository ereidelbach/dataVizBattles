#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 9 13:28:37 2019

@author: ejreidelbach

:DESCRIPTION: This script imports scrapes the data necessary for the October 
    2019 Data Viz Challenge.  The data is sourced from Where's the Jump?
    https://wheresthejump.com/full-movie-list/

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
path_dir = pathlib.Path('/home/ejreidelbach/Projects/dataVizBattles/2019-10/')
os.chdir(path_dir)
