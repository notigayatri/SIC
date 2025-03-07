import pymysql

class Db_operations:
    def __init__(self):
        pass

    def connect_db(self):
        try:
            connection=pymysql.Connect(host='localhost',port=3306,user='root',password='root',database='gayatri_db',charset='utf8')
            print("database connected")
            return connection
        except:
            print('database connection failed')
        
    def disconnect_db(self,connection):
        try:
            connection.close()
            print("database disconnected")
        except:
            print('database diconnection failed')

    def create_db(self):
        connection = self.connect_db()
        query = 'create database IF NOT EXISTS gayatri_db;'
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        print('DB created')

    def create_table(self):
        connection = self.connect_db()
        query = "create table IF NOT EXISTS person(id int primary key auto_increment, name varchar(32) not null, gender char check(gender in('m','M', 'f','F')), location varchar(32), dob date);"
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        print('Table created')
        self.disconnect_db(connection)


    def read_person_details(self):
        name = input('Enter person name: ')
        gender = input('Enter person gender: ')[0]
        location = input('Enter person location: ')
        dob = input('Enter person date of birth(yyyy-mm-dd): ')
        return (name, gender, location, dob)

    def insert_row(self):
        person = self.read_person_details()
        print(person)
        query = 'insert into person(name, gender, location, dob) values(%s, %s, %s, %s);'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query, person)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)

    def update_row(self):
        new_location = input('Enter new location of the person: ')
        id = int(input('Enter Id of the person to update the location: '))
        query = f'update person set location = {new_location} where id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)

    def delete_row(self):
        id = int(input('Enter Id of the person to delete: '))
        query = f'delete from person where id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print(f'Person with id = {id} not found')
        else:
            print(f'Person with id = {id} deleted')
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)

    def search_row(self):
        id = int(input('Enter Id of the person to search: '))
        query = f'select * from person where id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print(f'Person with id = {id} not found')
        else:
            row = cursor.fetchone()
            print(f'Person details are \n', str(row))
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)

    def list_all_rows(self):
        query = f'select * from person;'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print(f'No rows found in the table')
        else:
            rows = cursor.fetchall()
            for row in rows:
                print(str(row))
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
