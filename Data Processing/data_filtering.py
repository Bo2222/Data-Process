import pandas as pd

#讀取Excel文件
df = pd.read_excel("Data Processing/cleaned_example.xlsx")    #確保cleaned_example.xlsx在當前工作目錄中
#檔案路徑要因應資料夾的新增而做改變

#篩選學籍總成績大於90的數據
high_scores = df[df['學籍總成績'] > 90]

test_result = df['學籍總成績'] > 90

#打印學籍總成績大於90的數據
print("學籍縱成績大於90的數據：")
print(high_scores)

print('測試錯誤的結果：')
print(test_result)