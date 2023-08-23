# -*- coding: utf-8 -*-
"""
Excel Automation - Assignment 2 solution

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

import os
import glob
import pandas as pd

os.chdir("D:\\Udemy\\Excel Automation\\assignment")

cwd = os.getcwd()

filenames = glob.glob(cwd+"\\*\\*xlsx")

consolidated = pd.DataFrame(columns = pd.read_excel(filenames[0]).columns)
for file in filenames:
    temp = pd.read_excel(file)
    consolidated = consolidated.append(temp, ignore_index = True)
    
consolidated.to_excel("consolidated.xlsx", index = False)    
    

        
