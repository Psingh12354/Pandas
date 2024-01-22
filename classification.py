import pandas as pd
print("Started")
df = pd.read_excel(r'C:\New folder (4)\ClassificationTesting_updated.xlsx',header=0)
pd.set_option('display.max_columns', None)
dim_list = ['dim','Dim']
tds_list = ['Sum','Total','Average','Avg','Percentage','%','Min','Max','Count<Distinct','/','Rank','RunningCount','RunningSum']                                                 
db_list = ['Count','+','-','*']
df['FLAG'] = df['drill down'].apply(lambda x: 'TWB' if any([k in str(x) for k in tds_list]) else ('DB' if any([k in str(x) for k in db_list]) else 'Manual'))
print("Writting")
df.to_excel(r'C:\New folder (4)\Testing_v0.xlsx',index=False)
print("Done")
