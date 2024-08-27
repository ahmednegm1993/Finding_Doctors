import pandas as pd

df=pd.read_excel(r'E:\\Data_analysis_projects\\Finding Doctors\dataset\\employee_list_dummy_data.xlsx')
df1=df[df['last_name']=='Johnson'][['first_name','last_name']]
print(df1)