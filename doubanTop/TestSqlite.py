import sqlite3

conn=sqlite3.connect("test.db")
print("成功打开数据库")
c=conn.cursor()
sql='''
  select id,name,age from company

'''

# sql2='''
#   insert into company (id,name,age,address,salary)
#     values (2,"小紫",30,"程度",70000);
#
# '''

cur=c.execute(sql)
for row in cur:
    print(row)
    print(type(row))

conn.close()

print("执行成功")
