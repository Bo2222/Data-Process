import pandas as pd

#讀取已處理的Excel文件
df = pd.read_excel("Data Processing/cleaned_example.xlsx")    #確保cleaned_example.xlsx在當前工作目錄中
#檔案路徑要因應資料夾的新增而做改變

#按年齡分組
grouped = df.groupby('年齡')

#分別印出14歲和15歲的同學資料
print("14歲的同學：")
print(grouped.get_group(14))

print("\n15歲的同學：")
print(grouped.get_group('15'))