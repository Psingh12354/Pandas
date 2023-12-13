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

### Useful content
- [Toward data science](https://towardsdatascience.com/pandas-equivalent-of-10-useful-sql-queries-f79428e60bd9)

```bash
pip install markdown
```

```python
import markdown
html = markdown.markdown(your_text_string)
```

```python
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

```python

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

```python
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
```python
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
```python
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

```python
# The pandas explode() method is used to transform each element of a list-like structure (such as Python lists, tuples, sets, or NumPy arrays) to a separate row.
df.to_excel('C:\Sample Data\Python1.xlsx',index=False)
  
df = pd.read_excel(r'C:\Sample Data\Book4.xlsx',header=1)
  
df['ColName'] = df['ColName'].str.split(', ')
  
df= df.explode('ColName')
  
df.to_excel('C:\Sample Data\Python1.xlsx',index=False)
```

### Combining dataframe

```python
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

```python
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
```python
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
```python
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
# to put some conditions while using group by like below code return abs mean
df.groupby(['Region','Category'])['Profit'].apply(lambda x: abs(x.mean()))
```

### Assignment
```python
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

```python
import os
os.getcwd()
os.chdir('C:\\Sample Data\\')
os.rmdir('')
os.system('') # to open a file using python
os.path.join(cwd,'Sample Data','Folder 1') # we can define the path
import glob
# glob is to import multiple file like below * is wildcard for all
filenames = glob.glob('*')
# it means start with any ends with any but in between it must have 2016
filenames = glob.glob('*2016*')
# to get all file with any extension like .xlsx
glob.glob(cwd+'\\*\\*\\*.xlsx')
```

### To list down all file in multiple folder according to there name pattern.
```python
import os
import glob

os.chdir("D:\\Udemy\\Excel Automation\\assignment")

cwd = os.getcwd()

filenames = glob.glob("*.xlsx")

for file in filenames:
    year = file.split(".")[-2][-4:] # start from 2nd index in list and perform slicing
    try:
        int(year)
    except:
        continue
    if os.path.isdir(year) == False:
        os.mkdir(year)
    
    os.rename(file,os.path.join(cwd,year,file))
```
# to get data from multiple source and merge it in one excel.
```python
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
```

### To delete a specific row with specific value from excel

```python
df = pd.DataFrame(mydataset)
df
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2

i = df[df.cars=='Volvo'].index
i
Index([1], dtype='int64')
df.drop(i)
   cars  passings
0   BMW         3
2  Ford         2
```
### Distinct or unique to get unique value.

```python
df.cars.unique()
array(['BMW', 'Volvo', 'Ford'], dtype=object)
#or
np.unique(df[['col1','col2']], axis=0)
#
df.nunique()
cars        3
passings    3
dtype: int64
```
### to drop duplicates
```python
df.drop_duplicates()
```

### VLOOKUP in python
```python
import os
import pandas as pd

os.chdir("D:\\Udemy\\Excel Automation")

sales = pd.read_excel("sales_data.xlsx") #importing left dataframe

zip_income = pd.read_csv("zipcode_income.csv", engine='python') # importing right dataframe

temp = sales.merge(zip_income.loc[:,["Zip_Code","Mean"]].rename(columns={"Zip_Code":"Postal Code", "Mean":"Mean Income"})
                   ,how="left",on="Postal Code") # merging the left df with relevant columns of the right df

temp.drop_duplicates(subset=["Row ID"], keep ="first", inplace=True) # dropping duplicates
```

### IF condition
```python
# excel
=IF(O2="Bookcases",U2*0.8,IF(O2="Chairs",U2*10))
# Python
import numpy as np
df["Profit Percent"]=np.where(df['Category']=='Furniture',df['Per Units Sales']*0.5,np.where(df['Category']=='Office Supplies',df['Per Units Sales']*0.7,0))
#or
df['visits_category'] = np.where(df['visits_30days']== 0, 'YES', 'NO')
```

## Some more operations
```py
#Ordered dataframe
df['Order ID']
0       CA-2016-152156
1       CA-2016-152156
2       CA-2016-138688
3       US-2015-108966
4       US-2015-108966
             ...      
9989    CA-2014-110422
9990    CA-2017-121258
9991    CA-2017-121258
9992    CA-2017-121258
9993    CA-2017-119914
Name: Order ID, Length: 9994, dtype: object
```
### Slicing
```py
df['Order ID'].str[3:7]
0       2016
1       2016
2       2016
3       2015
4       2015
        ... 
9989    2014
9990    2017
9991    2017
9992    2017
9993    2017
Name: Order ID, Length: 9994, dtype: object

df['Order ID'].str[-7:]
0       -152156
1       -152156
2       -138688
3       -108966
4       -108966
         ...   
9989    -110422
9990    -121258
9991    -121258
9992    -121258
9993    -119914
Name: Order ID, Length: 9994, dtype: object

df['Order ID'].str[:2]
0       CA
1       CA
2       CA
3       US
4       US
        ..
9989    CA
9990    CA
9991    CA
9992    CA
9993    CA
Name: Order ID, Length: 9994, dtype: object
```

### Split
```
df['Order ID'].str.split('-')
0       [CA, 2016, 152156]
1       [CA, 2016, 152156]
2       [CA, 2016, 138688]
3       [US, 2015, 108966]
4       [US, 2015, 108966]
               ...        
9989    [CA, 2014, 110422]
9990    [CA, 2017, 121258]
9991    [CA, 2017, 121258]
9992    [CA, 2017, 121258]
9993    [CA, 2017, 119914]
Name: Order ID, Length: 9994, dtype: object
```

### Split indexing
```py
df['Order ID'].str.split('-')[1]
['CA', '2016', '152156]
```

### Removing extra spaces trim
```py
df['Order ID'].str.strip()
0       CA-2016-152156
1       CA-2016-152156
2       CA-2016-138688
3       US-2015-108966
4       US-2015-108966
             ...      
9989    CA-2014-110422
9990    CA-2017-121258
9991    CA-2017-121258
9992    CA-2017-121258
9993    CA-2017-119914
Name: Order ID, Length: 9994, dtype: object
```
### Concatenate
```py
df['location'] = df['Country']+"_"+df["City"]
```
### Upper and lower
```py
df['Category'].str.upper()
   
0             FURNITURE
1             FURNITURE
2       OFFICE SUPPLIES
3             FURNITURE
4       OFFICE SUPPLIES
             ...       
9989          FURNITURE
9990          FURNITURE
9991         TECHNOLOGY
9992    OFFICE SUPPLIES
9993    OFFICE SUPPLIES
Name: Category, Length: 9994, dtype: object

df['Category'].str.lower()
   
0             furniture
1             furniture
2       office supplies
3             furniture
4       office supplies
             ...       
9989          furniture
9990          furniture
9991         technology
9992    office supplies
9993    office supplies
Name: Category, Length: 9994, dtype: object
```

### Find
```py
df['Category'].str.find('Fur')
   
0       0
1       0
2      -1
3       0
4      -1
       ..
9989    0
9990    0
9991   -1
9992   -1
9993   -1
Name: Category, Length: 9994, dtype: int64

df['Category'].str.find('Fur').replace(-1,'Not Found')
   
0               0
1               0
2       Not Found
3               0
4       Not Found
          ...    
9989            0
9990            0
9991    Not Found
9992    Not Found
9993    Not Found
Name: Category, Length: 9994, dtype: object
```

# With conditions

```python
#Dataframe to excel
import os
import pandas as pd

os.chdir("D:\\Udemy\\Excel Automation") # changes working directory

sales_data = pd.read_excel("sales_data.xlsx")
```

### countif
```py
len(sales_data[sales_data["Quantity"] > 5])
sales_data[sales_data["Quantity"] > 5].shape[0]
```

### countifs
```py
len(sales_data[(sales_data["State"]=="Kentucky") & (sales_data["Quantity"] > 5)])
sales_data[(sales_data["State"]=="Kentucky") & (sales_data["Quantity"] > 5)].shape[0]
```
### sumif
```py
sales_data[sales_data["City"].str[:4]=="Fort"]["Profit"].sum()
sales_data.loc[sales_data["City"].str[:4]=="Fort","Profit"].sum()
```

### sumifs
```py
sales_data[(sales_data["City"].str[:4]=="Fort") & (sales_data["Quantity"] > 5)]["Profit"].sum()
sales_data.loc[(sales_data["City"].str[:4]=="Fort") & (sales_data["Quantity"] > 5),"Profit"].sum()
```

### loc & iloc [click here](https://discovery.cs.illinois.edu/guides/DataFrame-Fundamentals/dataframe-loc-vs-iloc/#:~:text=Difference%20Between%20loc%20and%20iloc,by%20one%20for%20each%20row)

```py
df.loc[0]
Row ID                                             1
Order ID                              CA-2016-152156
Order Date                       2016-11-08 00:00:00
Ship Date                        2016-11-11 00:00:00
Ship Mode                               Second Class
Customer ID                                 CG-12520
Customer Name                            Claire Gute
Segment                                     Consumer
Country                                United States
City                                       Henderson
Postal Code                                    42420
Region                                         South
Product ID                           FUR-BO-10001798
Category                                   Furniture
Sub-Category                               Bookcases
Product Name       Bush Somerset Collection Bookcase
Sales                                         261.96
Quantity                                           2
Discount                                         0.0
Profit                                       41.9136
Per Units Sales                               130.98

df.loc[0:10]
    Row ID        Order ID Order Date  ... Discount    Profit Per Units Sales
0        1  CA-2016-152156 2016-11-08  ...     0.00   41.9136        130.9800
1        2  CA-2016-152156 2016-11-08  ...     0.00  219.5820        243.9800
2        3  CA-2016-138688 2016-06-12  ...     0.00    6.8714          7.3100
3        4  US-2015-108966 2015-10-11  ...     0.45 -383.0310        191.5155
4        5  US-2015-108966 2015-10-11  ...     0.20    2.5164         11.1840
5        6  CA-2014-115812 2014-06-09  ...     0.00   14.1694          6.9800
6        7  CA-2014-115812 2014-06-09  ...     0.00    1.9656          1.8200
7        8  CA-2014-115812 2014-06-09  ...     0.20   90.7152        151.1920
8        9  CA-2014-115812 2014-06-09  ...     0.20    5.7825          6.1680
9       10  CA-2014-115812 2014-06-09  ...     0.00   34.4700         22.9800
10      11  CA-2014-115812 2014-06-09  ...     0.20   85.3092        189.5760

df.iloc[[1,4]]
   Row ID        Order ID Order Date  ... Discount    Profit Per Units Sales
1       2  CA-2016-152156 2016-11-08  ...      0.0  219.5820         243.980
4       5  US-2015-108966 2015-10-11  ...      0.2    2.5164          11.184

# choosing specific column till certain range
df.iloc[1:6,[1,4]]
         Order ID       Ship Mode
1  CA-2016-152156    Second Class
2  CA-2016-138688    Second Class
3  US-2015-108966  Standard Class
4  US-2015-108966  Standard Class
5  CA-2014-115812  Standard Class

# choosing n row with slicing on column
df.iloc[1:10,2:]
  Order Date  Ship Date       Ship Mode  ... Discount    Profit Per Units Sales
1 2016-11-08 2016-11-11    Second Class  ...     0.00  219.5820        243.9800
2 2016-06-12 2016-06-16    Second Class  ...     0.00    6.8714          7.3100
3 2015-10-11 2015-10-18  Standard Class  ...     0.45 -383.0310        191.5155
4 2015-10-11 2015-10-18  Standard Class  ...     0.20    2.5164         11.1840
5 2014-06-09 2014-06-14  Standard Class  ...     0.00   14.1694          6.9800
6 2014-06-09 2014-06-14  Standard Class  ...     0.00    1.9656          1.8200
7 2014-06-09 2014-06-14  Standard Class  ...     0.20   90.7152        151.1920
8 2014-06-09 2014-06-14  Standard Class  ...     0.20    5.7825          6.1680
9 2014-06-09 2014-06-14  Standard Class  ...     0.00   34.4700         22.9800

# some condition
df.loc[df['Ship Mode']=='Second Class']
      Row ID        Order ID Order Date  ... Discount    Profit Per Units Sales
0          1  CA-2016-152156 2016-11-08  ...      0.0   41.9136         130.980
1          2  CA-2016-152156 2016-11-08  ...      0.0  219.5820         243.980
2          3  CA-2016-138688 2016-06-12  ...      0.0    6.8714           7.310
17        18  CA-2014-167164 2014-05-13  ...      0.0    9.9900          27.750
18        19  CA-2014-143336 2014-08-27  ...      0.0    2.4824           4.280
...      ...             ...        ...  ...      ...       ...             ...
9965    9966  CA-2016-146374 2016-12-05  ...      0.0    2.3406           4.980
9966    9967  CA-2016-146374 2016-12-05  ...      0.0   51.5543          15.670
9980    9981  US-2015-151435 2015-09-06  ...      0.0   22.3548          85.980
9989    9990  CA-2014-110422 2014-01-21  ...      0.2    4.1028           8.416

# with 2 condition and(&)
df.loc[(df['Region']=='South') & (df['Category']=='Furniture')]

# with 2 condition or(|)
df.loc[(df['Region']=='South') | (df['Category']=='Furniture')]
```

### Matplotlib

```python
import matplotlib.pyplot as plt
import numpy as np
flg = plt.figure()
# it means we are creating axis starting from 0 to 1
ax = flg.add_axes([0,0,1,1])
x=np.arange(1,10)
# we can see a simple plot by below code.
ax.plot(x,x**2)
```
### Sort values
```python
df.loc[:,['Profit','Order ID']].sort_values(by=['Order ID'])
        Profit        Order ID
2717  109.6113  CA-2014-100006
6288   68.8464  CA-2014-100090
6287  -87.9354  CA-2014-100090
9514   31.8696  CA-2014-100293
3083    1.3257  CA-2014-100328
...        ...             ...
5932    1.0044  US-2017-169551
5933    4.8231  US-2017-169551
5934   85.7870  US-2017-169551
5929  -45.3492  US-2017-169551
5931 -113.9980  US-2017-169551

df.loc[:,['Profit','Order ID']].sort_values(by=['Order ID'],ascending=True)
        Profit        Order ID
2717  109.6113  CA-2014-100006
6288   68.8464  CA-2014-100090
6287  -87.9354  CA-2014-100090
9514   31.8696  CA-2014-100293
3083    1.3257  CA-2014-100328
...        ...             ...
5932    1.0044  US-2017-169551
5933    4.8231  US-2017-169551
5934   85.7870  US-2017-169551
5929  -45.3492  US-2017-169551
5931 -113.9980  US-2017-169551

[9994 rows x 2 columns]

df.loc[:,['Profit','Order ID']].sort_values(by=['Order ID'],ascending=False)
        Profit        Order ID
5934   85.7870  US-2017-169551
5933    4.8231  US-2017-169551
5930    5.4432  US-2017-169551
5931 -113.9980  US-2017-169551
5932    1.0044  US-2017-169551
...        ...             ...
3083    1.3257  CA-2014-100328
9514   31.8696  CA-2014-100293
6287  -87.9354  CA-2014-100090
6288   68.8464  CA-2014-100090
2717  109.6113  CA-2014-100006
```
### Drop Duplicates
```python
df.loc[:,['Profit','Order ID']].drop_duplicates()
```

### Libraries required for all below
```python
import pandas as pd
import os 
import numpy as np
import glob
import subprocess,openpyxl
from openpyxl import load_workbook
import re
from zipfile import ZipFile
import os
```

### Merging data of whole folder excel into one excel
```python
all_data = pd.DataFrame()
# Specify the folder containing your Excel files
folder_path = "C:\\\Python Merge" 
file_list = glob.glob(folder_path + "/*.xlsx")
count = 0
 
for i in file_list: 
    print(i)
    df = pd.read_excel(i, header=0, sheet_name='Attribute Level Metadata')
    print('after if')
    all_data = all_data._union(df, ignore_index=True)
    print('all data')
    count += 1
print('outside loop')
output_file_path = f"{folder_path}\\final.xlsx"
all_data.to_excel(output_file_path, sheet_name='Sheet1', index=False)
 
print("Data merged and saved to", output_file_path)
```

### Column wise split of data into multiple excel
```python
#original
package='Meta Split'
data_df = pd.read_excel(r"C:\package15.xlsx",header=0,sheet_name='Attribute Level Metadata')
parent = 'C:\\Chubb Jar COG\\pack\\'
path=os.path.join(parent,package)
os.mkdir(path)
grouped_df = data_df.groupby('SPECIFICATION_PACKAGE')
for data in grouped_df:
    grouped_df.get_group(data[0]).to_excel(f"Chubb Jar COG\\pack\\{package}\\"+data[0]+".xlsx",index=False)
```

### Processing Jars using python
```python
folder = 'C:\\Python Dup\\'
jarFile = f'{folder}Jar File'
base = f'{folder}excel\\template.xlsx'
file_list = glob.glob(folder + "/*.zip")
for i in range(len(file_list)):
    data = file_list[i].split('.')[0]
    wb=openpyxl.load_workbook(base)
    output_excel = f'{data}.xlsx'
    wb.save(output_excel)
    print(output_excel)
    try:
        cmd = f'cmd /c java -jar "{jarFile}" "{file_list[i]}" "{output_excel}"'
        subprocess.run(cmd,shell=True,check=True)
    except Exception as e:
        print(f'{data} {e}')
```

### Zipping multiple files in one go

```python
import zipfile
import os
 
def zip_files_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".xml"):
            file_name_1 = file_name.split('.')[0]
            file_path = os.path.join(folder_path, file_name)
            zip_file_path = os.path.join(folder_path, f"{file_name_1}.zip")
 
            with zipfile.ZipFile(zip_file_path, 'w',zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.write(file_path, file_name)
 
if __name__ == "__main__":
    folder_path = "C:\\Python Dup"  # Replace with your actual folder path
    zip_files_in_folder(folder_path)
```

### Comparing 2 folder and append the data if not exist in 2nd folder if exist it append
```python
# package='Meta Split_4'
# path=os.path.join("C:\\Merge",package)
# os.mkdir(path)
# file_list = os.listdir(folder_path)
# file_list_1 = os.listdir(folder_path_1)
folder_path = "C:\\Meta\\Meta Split_2"
file_list = glob.glob(folder_path + "/*.xlsx")
folder_path_1 = "C:\\Meta\\Meta Split_3"
file_list_1 = glob.glob(folder_path_1 + "/*.xlsx")
count=0
for i in file_list:
    data1 = i.split('\\')[-1].strip('.xlsx')
    for j in file_list_1:
        data2 = j.split('\\')[-1].strip('.xlsx')
        if data1==data2:
            count+=1
            try:
                df1 = pd.read_excel(i, header=0)
                df2 = pd.read_excel(j, header=0)
                df3 = df1._append(df2, ignore_index=True)
                df3= df3.drop_duplicates()
                path = f"C:\\Meta\\Meta Split_4\\{data2}.xlsx"
                df3.to_excel(path, sheet_name='Sheet1', index=False)
            except Exception as e:
                print(e)
        else:
            print("else"+data2)
print(count)
```

### Get non distinct value in python
```python
df1=df[df.duplicated(subset=['REPORT_NAME','ATTRIBUTE_NAME',keep=False)].drop_duplicates().sort_values('REPORT_NAME')
```

### Count
```python
df2 = pd.DataFrame(columns=['Package','Report_Count','Required Report'])
file_list_1 = glob.glob('C:\dump' + "/*.xlsm")
for i in file_list_1:
    print(i)
    file_name = i.split('\\')[-1]
    file_name = re.sub('.xlsm','',file_name)
    wb = openpyxl.load_workbook(i,read_only=True,keep_vba=True)
    sheet = wb['Summary']
    c7 = sheet['C7'].value
    c9 = sheet['C9'].value
    df2 = df2._append({'Package':file_name,'Report_Count':c7,'Required Report':c9},ignore_index=True)
df2.to_excel(r'C:\\Report Count Sheet\\cog_count_9.xlsx',index=False)
```

### Report Duplicate handle 
```python
all_data = pd.DataFrame()
 
# Specify the folder containing your Excel files
folder_path = "C:\\testing 2.0"
file_list = glob.glob(folder_path + "/*.xlsx")
count = 0

for i in file_list: 
    print(i)
    df = pd.read_excel(i, header=0, sheet_name='Attribute Level Metadata')
    # print('after if')
    # print(len(df))
    # #print(df.columns.values)
    # print("Report Name Unique Count : ",len(df['REPORT_NAME'].unique()))
    # print("Report Description Unique Count : ",len(df['REPORT_DESCRIPTION'].unique()))
    all_data=all_data.drop_duplicates()
    df = df.drop_duplicates()
    if 'REPORT_NAME' in all_data.columns:
        # Update report names with the appropriate suffix for instances in the second file
        report_names_set = set(all_data['REPORT_NAME'])
    # Update report names with the appropriate suffix
        for index, row in df.iterrows():
            report_name = row['REPORT_NAME']
            if report_name in report_names_set:
                # suffix_count = list(df['REPORT_NAME']).count(report_name)
                # suffix = '_1' if suffix_count==1 else f"_{suffix_count+1}"
                df.at[index, 'REPORT_NAME'] += f"_1"
                count=2
                while True:
                    if df.at[index, 'REPORT_NAME'] in report_names_set:
                        df.at[index, 'REPORT_NAME'] += f"_{count}"
                        print(df.at[index, 'REPORT_NAME'])
                        count+=1
                    else:
                        break
    all_data = all_data._append(df, ignore_index=True)
    # print('all data')
    # print(len(all_data))
print('outside loop')
#output_file_path = f"{folder_path}\\final.xlsx"
output_file_path = f"{folder_path}"
print("Unique REPORT_NAME in final package : ",len(all_data['REPORT_NAME'].unique()))
print("Unique REPORT_DESCRIPTION in final package : ",len(all_data['REPORT_DESCRIPTION'].unique()))
# row_limit = 1000000
# with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
#     start_row=0
#     for i in range(0, len(all_data), row_limit):
#         df_chunk = all_data.iloc[i:i + row_limit]
#         sheet_name = f'Sheet{i // row_limit + 1}'
#         df_chunk.to_excel(writer, sheet_name=sheet_name, startrow=start_row, index=False, header=True)
#         start_row += len(df_chunk) + 1

rows_per_file = 1000000
number_of_files = ((len(all_data)//rows_per_file))+1
start_index=0
end_index = rows_per_file
for i in range(number_of_files):
    filepart = f'{folder_path}\\final_{i}.xlsx'
    writer = pd.ExcelWriter(filepart)
    df_mod = all_data.iloc[start_index:end_index]
    df_mod.to_excel(writer, index=False, sheet_name='sheet')
    start_index = end_index
    end_index = end_index + rows_per_file
    writer.close()
print("Data merged and saved to", output_file_path)
```

### Updated above code to track the changes
```python
all_data = pd.DataFrame()
 
# Specify the folder containing your Excel files
folder_path = "C:\\Testing New"
file_list = glob.glob(folder_path + "/*.xlsx")
count = 0
df2 = pd.DataFrame(columns=['Package','Orig_Report_Name','New_Report_Name','Report_Desc','Specification_Pack'])
for i in file_list: 
    print(i)
    df = pd.read_excel(i, header=0, sheet_name='Attribute Level Metadata')
    # print('after if')
    # print(len(df))
    # #print(df.columns.values)
    # print("Report Name Unique Count : ",len(df['REPORT_NAME'].unique()))
    # print("Report Description Unique Count : ",len(df['REPORT_DESCRIPTION'].unique()))
    all_data=all_data.drop_duplicates()
    df = df.drop_duplicates()
    file_name = i.split('\\')[-1]
    file_name = re.sub('.xlsx','',file_name)
    if 'REPORT_NAME' in all_data.columns:
        # Update report names with the appropriate suffix for instances in the second file
        report_names_set = set(all_data['REPORT_NAME'])
    # Update report names with the appropriate suffix
        for index, row in df.iterrows():
            report_name = row['REPORT_NAME']
            if report_name in report_names_set:
                # suffix_count = list(df['REPORT_NAME']).count(report_name)
                # suffix = '_1' if suffix_count==1 else f"_{suffix_count+1}"
                # rep_var = df.at[index, 'REPORT_NAME']
                #df.at[index, 'REPORT_NAME'] += f"_1"
                # nrep_var = df.at[index, 'REPORT_NAME']
                # report_desc = df.at[index,'REPORT_DESCRIPTION']
                # attribute_agg = df.at[index,'ATTRIBUTE_AGGREGATION']
                #df2 = df2._append({'Package':file_name,'Orig_Report_Name':rep_var,'New_Report_Name':nrep_var,'Specification_Pack':attribute_agg},ignore_index=True)
                count=1
                while True:
                    if df.at[index, 'REPORT_NAME'] in report_names_set and count>1:
                        df.at[index, 'REPORT_NAME']= df.at[index, 'REPORT_NAME'][:-2]+f"_{count}"
                        # df.at[index, 'REPORT_NAME']+= f"_{count}"
                        print('count 2',df.at[index, 'REPORT_NAME'])
                        rep_var = df.at[index, 'REPORT_NAME']
                        nrep_var = df.at[index, 'REPORT_NAME']
                        report_desc = df.at[index,'REPORT_DESCRIPTION']
                        attribute_agg = df.at[index,'ATTRIBUTE_AGGREGATION']
                        df2 = df2._append({'Package':file_name,'Orig_Report_Name':rep_var,'New_Report_Name':nrep_var,'Report_Desc':report_desc,'Specification_Pack':attribute_agg},ignore_index=True)
                        count+=1
                    elif df.at[index, 'REPORT_NAME'] in report_names_set and count==1:
                        df.at[index, 'REPORT_NAME'] += f"_1"
                        print('count 1',df.at[index, 'REPORT_NAME'])
                        nrep_var = df.at[index, 'REPORT_NAME']
                        nrep_var = df.at[index, 'REPORT_NAME']
                        report_desc = df.at[index,'REPORT_DESCRIPTION']
                        attribute_agg = df.at[index,'ATTRIBUTE_AGGREGATION']
                        df2 = df2._append({'Package':file_name,'Orig_Report_Name':rep_var,'New_Report_Name':nrep_var,'Report_Desc':report_desc,'Specification_Pack':attribute_agg},ignore_index=True)
                        count+=1
                    else:
                        break
    all_data = all_data._append(df, ignore_index=True)
    # print('all data')
    # print(len(all_data))
print('outside loop')
#output_file_path = f"{folder_path}\\final.xlsx"
output_file_path = f"{folder_path}"
print("Unique REPORT_NAME in final package : ",len(all_data['REPORT_NAME'].unique()))
print("Unique REPORT_DESCRIPTION in final package : ",len(all_data['REPORT_DESCRIPTION'].unique()))
df2.to_excel(r'C:\\Testing New\change.xlsx',index=False)
print('change sheet generated')
rows_per_file = 1000000
number_of_files = ((len(all_data)//rows_per_file))+1
start_index=0
end_index = rows_per_file
for i in range(number_of_files):
    filepart = f'{folder_path}\\final_{i}.xlsx'
    writer = pd.ExcelWriter(filepart)
    df_mod = all_data.iloc[start_index:end_index]
    df_mod.to_excel(writer, index=False, sheet_name='sheet')
    start_index = end_index
    end_index = end_index + rows_per_file
    writer.close()
print("Data merged and saved to", output_file_path)
```
