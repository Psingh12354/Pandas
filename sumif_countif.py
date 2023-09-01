# -*- coding: utf-8 -*-
"""
Excel Automation - sumif(s) and countif(s)

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

import os
import pandas as pd

os.chdir("D:\\Udemy\\Excel Automation") # changes working directory

sales_data = pd.read_excel("sales_data.xlsx")

#countif
len(sales_data[sales_data["Quantity"] > 5])
sales_data[sales_data["Quantity"] > 5].shape[0]


#countifs
len(sales_data[(sales_data["State"]=="Kentucky") & (sales_data["Quantity"] > 5)])
sales_data[(sales_data["State"]=="Kentucky") & (sales_data["Quantity"] > 5)].shape[0]

#sumif
sales_data[sales_data["City"].str[:4]=="Fort"]["Profit"].sum()
sales_data.loc[sales_data["City"].str[:4]=="Fort","Profit"].sum()

#sumifs
sales_data[(sales_data["City"].str[:4]=="Fort") & (sales_data["Quantity"] > 5)]["Profit"].sum()
sales_data.loc[(sales_data["City"].str[:4]=="Fort") & (sales_data["Quantity"] > 5),"Profit"].sum()