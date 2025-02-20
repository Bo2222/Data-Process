import pandas as pd

#讀取Excel文件
file_path = 'File Processing/示範檔案.xlsx'
excel_file = pd.ExcelFile(file_path)

#顯示原始工作表名稱
print("原始工作表名稱：")
print(excel_file.sheet_names)

#修改工作表名稱
new_sheet_names = {}
for sheet in excel_file.sheet_names:
    new_name = f"2025年{sheet}"
    new_sheet_names[sheet] = new_name

#複製原始數據到新的工作表
with pd.ExcelWriter('File Processing/修改後的檔案.xlsx', engine = 'openpyxl') as writer:
    for sheet in excel_file.sheet_names:
        #讀取原始工作表數據
        df = pd.read_excel(file_path, sheet_name = sheet)
        #將數據寫入新的工作表名稱
        df.to_excel(writer, sheet_name  = new_sheet_names[sheet], index = False)

#顯示修改後的工作表名稱
modified_excel_file = pd.ExcelFile('File Processing/修改後的檔案.xlsx')
print("\n修改後的工作表名稱：")
print(modified_excel_file.sheet_names)