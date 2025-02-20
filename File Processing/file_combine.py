import pandas as pd
import os

#設定資料夾路徑
folder_path = 'File Processing/classed_file'    #資料夾名稱

#創建一個空的列表來存儲所有的Dataframe
all_dataframes = []

#遍歷資料夾中的所有Excel檔案
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)
        #讀取Excel檔案並將其添加到列表中
        df = pd.read_excel(file_path)
        all_dataframes.append(df)

#使用concat合併所有DataFrame
combined_df = pd.concat(all_dataframes, ignore_index=True)

#將合併後的DatatFrame保存為新的Excel檔案
combined_df.to_excel('File Processing/成績總表.xlsx', index = False)

print("所有學生成績已成功合併並保存為 成績總表.xlsx")