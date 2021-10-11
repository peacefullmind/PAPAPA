
# import pandas as pd
# import json
import demjson
import xlwt

f = open("data.txt","r",encoding="utf-8")
cont=f.read()
f.close()

print(cont)
print(type(cont))


data = demjson.decode(cont)
print(data)
print(type(data))

value=data['ROOT']
print(value)
print(type(value))
print(len(value))

file =xlwt.Workbook() #新建一个excel
table=file.add_sheet('输出结果')
table_row=0#这是行数，从0行开始写
table.write(table_row, 0, '编码')  # 将,,写入
table.write(table_row, 1, '公司')  # 将,,写入
table.write(table_row, 2, '状态')  # 将,,写入
# table.write(table_row, 3, '日期')  # 将,,写入
table_row=table_row+1

for row in value:
    print(row)
    print(type(row))
    bianma=row['ZBPCTYGSDM']
    name=row['ZBPCTYGSMC']
    zhuangtai=row['ZLOCK']
    table.write(table_row,0,bianma)
    table.write(table_row, 1, name)
    table.write(table_row, 2, zhuangtai)
    table_row=table_row+1

file.save('查询结果.xls')
