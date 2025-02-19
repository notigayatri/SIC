import pymysql
def connect_db():
    connection=pymysql.Connect(host='localhost',port=3306,user='root',password='root',database='gayatri_db',charset='utf8')
    print("database connected")
    return connection

def disconnect_db(connection):
    connection.close()
    print("database disconnected")

connection=connect_db()
disconnect_db(connection)