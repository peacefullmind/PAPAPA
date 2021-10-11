import pymongo

#获取连接mongodb的对象
client=pymongo.MongoClient("127.0.0.1",port=27017)

#获取数据库
db=client.test

#获取数据库的集合（类似于关系型数据库的表的概念）
collection=db.mess

#写入数据
# collection.insert_one({"username":"tao"})

#写入多条数据
# collection.insert_many([
#     {
#         "name":"小红",
#         "age": 18
#     },
#     {
#         "name":"小明",
#         "age": 20
#     }
# ])

#查找数据
# cursor=collection.find()
# for x in  cursor:
#     print(x)

#更新数据
collection.update_one({"age":20},{"$set":{"age":33}})
#此外还有update_many

# 删除 delete_one等类似