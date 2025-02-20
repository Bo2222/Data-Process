import pandas as pd

#生成數據
data = {
    "數據1": [1,2,3,4,5],
    "數據2": [5,4,3,2,1]
}

#建立Excel檔案並添加到工作表
with pd.ExcelWriter('File Processing/示範檔案.xlsx', engine='openpyxl') as writer:      #這邊也是要修改檔案路徑
    for month in ["1月", "2月", "3月"]:
        #創建DataFrame
        df = pd.DataFrame(data)
        #將DataFrame寫入工作表
        df.to_excel(writer, sheet_name=month, index=False)

print("示範Excel檔案已生成，包含工作表:1月, 2月, 3月")