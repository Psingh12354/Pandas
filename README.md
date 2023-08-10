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
