import pandas as pd

#讀取已處理的Excel文件（以學生年齡成績表為例）
df= pd.read_excel('Data Processing/cleaned_example.xlsx')

#按年齡分組
grouped = df.groupby('年齡')

#將14歲的學生資料保存到Excel檔案
df_14 = grouped.get_group(14)
df_14.to_excel('File Processing/students_age_14.xlsx', index=False)

#將15歲的學生資料保存到Excel檔案
df_15 = grouped.get_group(15)
df_15.to_excel('File Processing/students_age_15.xlsx', index=False)

print("已將學生資料依照年齡分組並保存為兩個Excel檔案。")