# Pandas [Link](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)

- To get one or more rows use loc
- df.to_string() to print entire dataframe
- Use head or tail to get first few value or last few value. ```df.tail()``` 
- To get info about the data use ```df.info()```
- to deal with empty cells is to remove rows that contain empty cells. ```df.dropna() or df.dropna(inplace = True)``` 2nd one will make the changes permanent.
- to get total number of rows ```len(df)```
- The fillna() method allows us to replace empty cells with a value ```df.fillna(130, inplace = True)```
- We can assign the column a same data type like ```df['Date'] = pd.to_datetime(df['Date'])```
- The duplicated() method returns a Boolean values for each row: ```print(df.duplicated())```
- 


```
import pandas
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

var = pandas.DataFrame(mydataset)
var
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2

df.loc[0]
cars        BMW
passings      3
Name: 0, dtype: object

df.loc[[0,1]]
    cars  passings
0    BMW         3
1  Volvo         7

```

```

import numpy as np
np_array = np.array([1,2,4,2])
np_array
array([1, 2, 4, 2])
pd_series = pd.Series(np_array)
pd_series
0    1
1    2
2    4
3    2
dtype: int32
pd_series = pd.Series(np_array,index=['a','b','c','d'])
                      
pd_series
                      
a    1
b    2
c    4
d    2
dtype: int32
pd_series['a]
          
SyntaxError: unterminated string literal (detected at line 1)
pd_series['a']
          
1
pd_series[['a','c']]
          
a    1
c    4
dtype: int32
```
### Excel
```
df = pd.read_excel(r'C:\Sample Data\data_1.xlsx')
# use sheet number starting from 0
df = pd.read_excel(r'C:\Sample Data\data_1.xlsx',sheet_name=0)
# by name
df = pd.read_excel(r'C:\Sample Data\data_1.xlsx',sheet_name='Orders')
# can define header startign from row 0
df = pd.read_excel(r'C:\Sample Data\data_1.xlsx',sheet_name='Orders',header=3)
# We can create any col as index col like below
df = pd.read_excel(r'C:\Sample Data\data_1.xlsx',sheet_name='Orders',header=3,index_col='Row ID')
# To get the data types
df.dtypes
# To perform basic statistical operation use below command
df.describe()
# to list down all the columns
df.columns
# BY DEFAULT Pandas drop a row
# by default inplace is false u need to define it true to make the changes visible to view level.
df.drop('State',axis=1,inplace=True)
# To add new column with certain operation
df['Per Units Sales'] = df['Sales']/df['Quantity']
# to write save the data in excel use below command
df.to_excel('Path/filename')
df.to_excel(r'C:\Sample Data\data_2.xlsx')
# If don't want to go with index drop in generated excel
df.to_excel(r'C:\Sample Data\data_3.xlsx',index=False)
# to display all the values

pd.set_option('display.max_columns', None)

# to change the dtypes

df['Postal Code'] = df['Postal Code'].astype(str)
```

### Date
```
# to format the order date
df['Order Date'] = pd.to_datetime(df['Order Date'],errors = 'raise',format = '%Y-%m-%d')
# to extract year similart 'month'
df['year'] = df['Order Date'].dt.year
# to get the shipping date
df["Shipping Date"] = df["Ship Date"] - df["Order Date"]
# small b and cap B represt nov and November like that 
df['String Date'] = df['Order Date'].dt.strftime('%B-%Y')
```

### Data
```
It checks whether it has any null or nan value and returns bool value
df.isna()
# to get the sum of all na values
df.isna().sum()
# row wise
df.isna().sum(axis=1)
# to get all the rows which has NAN values
df[df.isna().sum(axis=1)>0]
# how = any represent drop the row or col if it has null value
# if all single value of row and col is null use how = all
df.dropna(how='all',inplace=True)
# fillna
df.fillna(0,inplace=True)
```

### To split the excel row wise using explode

```
# The pandas explode() method is used to transform each element of a list-like structure (such as Python lists, tuples, sets, or NumPy arrays) to a separate row.
df.to_excel('C:\Sample Data\Python1.xlsx',index=False)
  
df = pd.read_excel(r'C:\Sample Data\Book4.xlsx',header=1)
  
df['ColName'] = df['ColName'].str.split(', ')
  
df= df.explode('ColName')
  
df.to_excel('C:\Sample Data\Python1.xlsx',index=False)
```

### Combining dataframe

```
nutrition = pd.DataFrame({"item":["pizza","pastry","burritto","salad","pasta"],
                         "avg_calorie":[3200,800,940,240,740],
                         "protein":["12%","4%","16%","6%","10%"]})
menu = pd.DataFrame({"item":["pizza","pasta","salad","burritto","taco","burger"],
                    "price":[14.99,12.99,7.99,10.99,6.99,5.99],
                    "popularity":["high","medium","low","high","medium","high"]})
# Concat will just concatenate the values. We can pass multiple dataset
pd.concat([menu,nutrition],axis=1,ignore_index=False)
# merge took common column and print the output work on intersection can perform left, right, outer and inner. by default inneer
menu.merge(nutrition) 

menu.merge(nutrition,how="inner")
       item  price popularity  avg_calorie protein
0     pizza  14.99       high         3200     12%
1     pasta  12.99     medium          740     10%
2     salad   7.99        low          240      6%
3  burritto  10.99       high          940     16%

menu.merge(nutrition,how="outer")
       item  price popularity  avg_calorie protein
0     pizza  14.99       high       3200.0     12%
1     pasta  12.99     medium        740.0     10%
2     salad   7.99        low        240.0      6%
3  burritto  10.99       high        940.0     16%
4      taco   6.99     medium          NaN     NaN
5    burger   5.99       high          NaN     NaN
6    pastry    NaN        NaN        800.0      4%

menu.merge(nutrition,how="left")
       item  price popularity  avg_calorie protein
0     pizza  14.99       high       3200.0     12%
1     pasta  12.99     medium        740.0     10%
2     salad   7.99        low        240.0      6%
3  burritto  10.99       high        940.0     16%
4      taco   6.99     medium          NaN     NaN
5    burger   5.99       high          NaN     NaN

menu.merge(nutrition,how="right")
       item  price popularity  avg_calorie protein
0     pizza  14.99       high         3200     12%
1    pastry    NaN        NaN          800      4%
2  burritto  10.99       high          940     16%
3     salad   7.99        low          240      6%
4     pasta  12.99     medium          740     10%

# use left on and right on if there is no common columns.
menu.merge(nutrition,how="right",left_on="items",right_on="item")

# Join is very similar to vlookup by default left

menu.join(nutrition)
      items  price popularity      item  avg_calorie protein
0     pizza  14.99       high     pizza       3200.0     12%
1     pasta  12.99     medium    pastry        800.0      4%
2     salad   7.99        low  burritto        940.0     16%
3  burritto  10.99       high     salad        240.0      6%
4      taco   6.99     medium     pasta        740.0     10%
5    burger   5.99       high       NaN          NaN     NaN

# to perform default join properly use set_index. Otherwise output look like above.
menu.set_index('items').join(nutrition.set_index('item'))
          price popularity  avg_calorie protein
items                                          
pizza     14.99       high       3200.0     12%
pasta     12.99     medium        740.0     10%
salad      7.99        low        240.0      6%
burritto  10.99       high        940.0     16%
taco       6.99     medium          NaN     NaN
burger     5.99       high          NaN     NaN
```

# How to check something is there in list or not

```
import pandas as pd
df = pd.DataFrame({'IDs':[1234,5346,1234,8793,8793],
                    'Names':['APPLE ABCD ONE','APPLE ABCD','NO STRAWBERRY YES','ORANGE AVAILABLE','TEA AVAILABLE']})

df
    IDs              Names
0  1234     APPLE ABCD ONE
1  5346         APPLE ABCD
2  1234  NO STRAWBERRY YES
3  8793   ORANGE AVAILABLE
4  8793      TEA AVAILABLE
lis = [ABCD, TEA]
df['Names'].apply(lambda x: any([k in x for k in lis]))
  
0     True
1     True
2    False
3    False
4     True
Name: Names, dtype: bool
df['FLAG']=df['Names'].apply(lambda x: any([k in x for k in lis]))
  
df
  
    IDs              Names   FLAG
0  1234     APPLE ABCD ONE   True
1  5346         APPLE ABCD   True
2  1234  NO STRAWBERRY YES  False
3  8793   ORANGE AVAILABLE  False
4  8793      TEA AVAILABLE   True

df['FLAG']=df['Names'].apply(lambda x: any([k in x for k in lis])).replace(True,'Fine').replace(False,'Not Fine')
df
  
    IDs              Names FLAG
0  1234     APPLE ABCD ONE  TDS
1  5346         APPLE ABCD  TDS
2  1234  NO STRAWBERRY YES   DB
3  8793   ORANGE AVAILABLE   DB
4  8793      TEA AVAILABLE  TDS
```

### Check of above back
```
import pandas as pd

df = pd.read_excel(r'C:\HEB KPI\Book1.xlsx',header=0)
               
df['Report Detail [Table,filed & calculations]'] = df['Report Detail [Table,filed & calculations]'].str.split('\n')

df= df.explode('Report Detail [Table,filed & calculations]')
       
df.to_excel('C:\LOCATION\Testing_v0.xlsx',index=False)

lis = [ABCD, TEA]

df['FLAG']=df['Names'].apply(lambda x: any([k in x for k in lis])).replace(True,'TDS').replace(False,'DB')

df.to_excel('C:\Sample Data\Python1.xlsx',index=False)

df1['FLAG']=df1['Report Detail'].apply(lambda x: any([k in str(x) for k in lis])).replace(True,'TDS').replace(False,'DB')

```

### Data Aggregation groupby
```
Excel approach- ALT + D + P + P to create a pivot table

# To get to count for all the columns
df.groupby('Region').count()
# To get sum of element in specific column
df.groupby(['Region'])['Profit'].sum()
Region
Central     39706.3625
East        91522.7800
South       46749.4303
West       108418.4489
Name: Profit, dtype: float64
# for grouping multiple value
df.groupby(['Region','Category'])['Profit'].sum()
Region   Category       
Central  Furniture          -2871.0494
         Office Supplies     8879.9799
         Technology         33697.4320
East     Furniture           3046.1658
         Office Supplies    41014.5791
         Technology         47462.0351
South    Furniture           6771.2061
         Office Supplies    19986.3928
         Technology         19991.8314
West     Furniture          11504.9503
         Office Supplies    52609.8490
         Technology         44303.6496
Name: Profit, dtype: float64
```

### Assignment
```
import pandas as pd
import numpy as np
df = pd.read_excel(r'C:\Sample Data\commute.xlsx',header=0,index_col="Date")
df
           Subway  Taxi  Bus Ferry
Date                              
2020-06-01    Yes     2    7   Yes
2020-06-02    Yes     1    9   Yes
2020-06-03    Yes     8   10   Yes
2020-06-04     No     8    8   Yes
2020-06-05     No     4    7   Yes
...           ...   ...  ...   ...
2020-11-06     No     4    8    No
2020-11-07    Yes     1    7   Yes
2020-11-08    Yes     7    7   Yes
2020-11-09     No     8   13   Yes
2020-11-10    Yes     5    7    No

[163 rows x 4 columns]
df.replace(['Yes','No'],[1,0])
  
            Subway  Taxi  Bus  Ferry
Date                                
2020-06-01       1     2    7      1
2020-06-02       1     1    9      1
2020-06-03       1     8   10      1
2020-06-04       0     8    8      1
2020-06-05       0     4    7      1
...            ...   ...  ...    ...
2020-11-06       0     4    8      0
2020-11-07       1     1    7      1
2020-11-08       1     7    7      1
2020-11-09       0     8   13      1
2020-11-10       1     5    7      0

[163 rows x 4 columns]
s = np.array(df)
s
df=df.replace(['Yes','No'],[1,0])
s = np.array(df)
s
y = np.array([8,3,0.5,12])
y
array([ 8. ,  3. ,  0.5, 12. ])
s.dot(y)
array([29.5, 27.5, 49. , 40. , 27.5, 16.5, 30. , 38.5, 29. , 28. , 32. ,
       30. , 30. , 48. , 33. , 45. , 38. , 28. , 24.5, 14. , 31. , 39. ,
       38. , 24.5, 30. , 36.5, 39. , 48.5, 30.5, 28. , 32. , 33. , 41.5,
       26.5, 25. , 20.5, 16.5, 21.5, 30.5, 27.5, 45. , 13. , 34.5, 21. ,
       44. , 39. , 18.5, 36.5, 33.5, 36.5, 17. , 10. , 27. , 19. , 18.5,
       42. , 46.5, 48.5, 39. , 26. , 21.5, 19.5, 26. , 48.5, 29.5, 24. ,
       29. , 12. , 17.5, 31.5, 18. , 39.5, 17. , 29. , 22.5, 48. , 19.5,
       33. , 15.5, 23. , 31. , 15. , 22.5, 23.5, 25.5, 39. ,  6. , 28.5,
       42. , 21.5, 22.5, 46.5, 15.5, 21.5, 29. , 28. , 29. , 18. , 34. ,
       35. , 30.5, 23. , 22.5, 37. , 45.5, 32.5,  7.5, 21. ,  7. , 32.5,
       37. , 23. , 14.5, 39.5, 14.5, 35. , 22. , 18. , 33.5, 40. , 16.5,
       19.5, 39.5, 17. , 19.5, 28. , 43. , 24.5, 43. , 24. , 25.5, 40. ,
       13. , 25.5, 24. , 27. , 46. , 30.5, 21. , 15. , 26. , 24. , 27.5,
       30. , 48. , 50.5, 40.5, 38.5, 25. , 13.5, 18.5, 27.5, 28. , 27. ,
       20. , 18. , 13. , 43.5, 16. , 26.5, 44.5, 42.5, 26.5])
daily_expense=s.dot(y)
daily_expense.sum()
4683.0
daily_expense.argmax()
145
df.index[daily_expense.argmax()]
Timestamp('2020-10-24 00:00:00')
```
### OS

```
import os
os.getcwd()
os.chdir('C:\\Sample Data\\')
os.rmdir('')
os.system('') # to open a file using python
os.path.join(cwd,'Sample Data','Folder 1') # we can define the path 
