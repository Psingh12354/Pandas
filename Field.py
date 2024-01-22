print('started')
import re
import pandas as pd
df = pd.read_excel(r'C:\Sample Data\FieldComment.xlsx',header=0)
file = open('C:/Python/DDL_Scripts_PCD_Output.txt','r')
file1 = open("C:/Python/Output.txt", "w")
srclist = file.readlines()
def getColCmt(tab_name, col_name):
    cmt = df.query(f"(TABLE_NAME == '{tab_name}') & (COLUMN_NAME == '{col_name}')")['COMMENTS'].values.tolist()
    cmt = [str(j) for j in cmt]
    cmt = [j for j in cmt if j != 'nan']
    if cmt:
        return cmt[0]
    else:
        return None
for i in range(len(srclist)):
    line = srclist[i]
    if '/*' in line and line:
        old_field_name = line.split()[0]
        comment=re.findall(r'/\*(.*?)\*/',line,re.IGNORECASE)[0].strip()
        comment_1=re.findall(r'/\*(.*?)\*/',line,re.IGNORECASE)[0].strip('--')
        if '.' in comment:
            field_name = comment.split('.')[-1]
            table_name = comment.split('.')[0]
            alias_name = line.split('as')[-1].split('/*')[0].strip()
            if len(field_name.split(' '))==1:
                new_field_name = field_name
                cmt= getColCmt(table_name,field_name)
                value=f'\t{new_field_name} as {alias_name} \t /* {cmt} */\n,'
                srclist[i]=value
                
            else:
                pass
       
        elif '-' in comment_1:
            field_name = comment_1.split('-')[-1].split(' ')[0]
            table_name = comment_1.split('-')[0]
            if len(field_name.split(' '))==1:
                new_field_name = field_name
                cmt= getColCmt(table_name,field_name)
                value=f'\t{new_field_name} as /* {cmt} */\n,'
                srclist[i]=value
            else:
                pass
    elif line.strip()=='FROM':
        srclist[i-1]=srclist[i-1].replace(',','')
        
        
file1.writelines(srclist)
file.close()
file1.close()
