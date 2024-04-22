from pymongo import MongoClient

host = 'localhost'
port = 3306
db = 'spider'
user = 'admin'
password = 'qwe123'

conn = MongoClient('localhost',27017)  #连接mangodb
db = conn.stu   #连接数据库
my_set = db.stu #连接集合
data = [{'name':'dongli','age':18},{'name':'wanzi','age':18},{'name':'xiaobai','age':28}]
my_set.insert_many(data) #如果报错了就试insert_one, insert_many


#查询语句
for data in my_set.find():
    print(data)