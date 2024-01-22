import pandas as pd    
xlsx_path = r'C:\New folder\Book1.xlsx'
exls = pd.ExcelFile(xlsx_path)
print('Reading')
df = pd.read_excel(exls,"Sheet1")
df = df.applymap(lambda x: x.strip() if type(x)==str else x)
col = list(df.columns)
print('Started')
for i in range(len(col)):
    unq = col[0:i+1]
    temp_df = df.groupby(unq).size().reset_index(name='count')
    temp_df.drop(['count'], axis=1, inplace=True)
    li = temp_df.values.tolist()
    for j in li:
        li1 = (len(col)-(i+1))*[float('NaN')]
        li2 = j + li1 
        df.loc[len(df)] = li2
    if i == 7:
        break
df2 = df.sort_values(list(df.columns), ascending=False)
df2 = df2.drop_duplicates()
df2 = df2.iloc[::-1]
print("Writing Started")
xlsx_path_2 = r'C:\New folder\SuperSub.xlsx'
with pd.ExcelWriter(xlsx_path_2) as writer: 
     df2.to_excel(writer, sheet_name='Sheet2', index = False)

