# -*- coding: utf-8 -*-
"""
Excel Automation - Assignment 1 solution

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

import os
import glob

os.chdir("D:\\Udemy\\Excel Automation\\assignment")

cwd = os.getcwd()

filenames = glob.glob("*.xlsx")

for file in filenames:
    year = file.split(".")[-2][-4:]
    try:
        int(year)
    except:
        continue
    if os.path.isdir(year) == False:
        os.mkdir(year)
    
    os.rename(file,os.path.join(cwd,year,file))
        
