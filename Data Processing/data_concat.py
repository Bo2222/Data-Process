import pandas as pd

#讀取已處理過的Excel文件
df = pd.read_excel("Data Processing/cleaned_example.xlsx")    #確保cleaned_example.xlsx在當前工作目錄中
#檔案路徑要因應資料夾的新增而做改變

#新增班級成員
new_student = pd.DataFrame({
    '名字': ['Roni'],
    '年齡': [15],
    '學籍總成績': [100]
})

#將新學生資料添加到原有的DataFrame
df = pd.concat([df, new_student], ignore_index=True)

#打印合併後的結果
print("合併後的結果：")
print(df)
