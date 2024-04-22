import pymysql

host = 'localhost'
port = 3306
db = 'spider'
user = 'admin'
password = 'qwe123'

conn = pymysql.connect(host=host,port = port,db=db,user=user,password=password)
cursor = conn.cursor()

# 插入数据
cursor.execute("insert into product(id,name,price) values(3,'hp',8000);")
conn.commit()

cursor.execute('select * from product')
print(cursor.fetchall())

cursor.close()
conn.close()