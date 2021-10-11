import os
import pandas as pd

file_path= '/PYcode/PAPAPA/Tripadvisor/评论/'
file_names=os.listdir(file_path)
print(file_names)
file_merge=pd.DataFrame()
for name in file_names:
    print(file_path+name)
    df=pd.read_excel(file_path+name)
    file_merge=file_merge.append(df)
file_merge.to_excel('/PYcode/PAPAPA/Tripadvisor/评论/total.xlsx',index=None)