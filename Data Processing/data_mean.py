import pandas as pd

#讀取已處理過的excel文件
df = pd.read_excel("Data Processing/cleaned_example.xlsx")    #確保cleaned_example.xlsx在當前工作目錄
#檔案路徑要因應資料夾的新增而做改變

#計算學籍總成績平均值
average_score = df['學籍總成績'].mean()

#打印平均成績
print(f"班級的學籍總成績平均為：{average_score:.2f}")
