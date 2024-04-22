import pymysql

host = 'localhost'
port = 3306
db = 'spider'
user = 'admin'
password = 'qwe123'

conn = pymysql.connect(host=host,port = port,db=db,user=user,password=password)
cursor = conn.cursor()
cursor.execute('select * from product')
print(cursor.fetchone())
print(cursor.fetchall())
cursor.close()
conn.close()

