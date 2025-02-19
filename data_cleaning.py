import pandas as pd

#讀取Excel文件
df = pd.read_excel('example.xlsx')      #確保example.xlsx在當前工作目錄中

#讀取原始數據
print("原始數據：")
print(df)

#將沒有名字的單元格填充為”無民氏“
df['名字'].fillna("無名氏", inplace=True)

#將學籍總成績為空的單元格填充為60
df['學籍總成績'].fillna(60, inplace=True)

#刪除重複行
df_cleaned = df.drop_duplicates()

#顯示清理後的數據
print("\n清理後的數據：")
print(df_cleaned)

#將清理後的數據保存到新的Excel文件
df_cleaned.to_excel('cleaned_example.xlsx', index=False)