import pymysql
def connect_db():
    try:
        connection=pymysql.Connect(host='localhost',port=3306,user='root',password='root',database='gayatri_db',charset='utf8')
        print("database connected")
        return connection
    except:
        print('database connection failed')
    
def disconnect_db(connection):
    try:
        connection.close()
        print("database disconnected")
    except:
        print('database diconnection failed')

connection=connect_db()
if connection:
    disconnect_db(connection)
