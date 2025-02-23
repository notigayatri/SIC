import pymysql

class Flight:
    def __init__(self, flight_number="", airline="", departure="", arrival=""):
        self.flight_number  = flight_number
        self.airline        = airline
        self.departure      = departure
        self.arrival        = arrival

    def __str__(self):
        print(f'flight_number:{self.flight_number}, airline:{self.airline}')

class Db_operations:
    def __init__(self):
        pass

    def connect_db(self):
        try:
            connection = pymysql.Connect(host='localhost', port=3306, user='root', password='root', database='gayatri_db', charset='utf8')
            print('DB connected')
            return connection
        except:
            print('DB connection failed')

    def disconnect_db(self, connection):
        try:
            connection.close()
            print('DB dis-connected')
        except:
            print('Error while disconnecting DB')

    def create_db(self):
        connection = self.connect_db()
        query = 'create database IF NOT EXISTS gayatri_db;'
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        print('DB created')
        self.disconnect_db(connection)

    def create_table(self):
        connection = self.connect_db()
        query = "create table IF NOT EXISTS flights(id int primary key auto_increment, flight_number varchar(10) not null unique, airline varchar(50) not null, departure varchar(50) not null, arrival varchar(50) not null );"
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        print('Table created')
        self.disconnect_db(connection)

    def read_flight_details(self):
        flight_number= input('Enter flight number: ')
        airline = input('Enter flight name: ')[0]
        departure = input('Enter departure airport: ')
        arrival= input('Enter arrival airport: ')
        return (flight_number,airline, departure, arrival)

    def insert_row(self, flight):
        query = 'insert into flights(flight_number, airline, departure, arrival) values(%s, %s, %s, %s);'
        flight_tuple = (flight.flight_number, flight.airline, flight.departure, flight.arrival)
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query, flight_tuple)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        id = self.get_latest_row_id()
        return id

    def update_row(self, data):
        query = f'update flights set flight_number = %s, airline = %s, departure = %s, arrival = %s where id = %s'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)

    def delete_row(self, id):
        #id = int(input('Enter Id of the person to delete: '))
        query = f'delete from flights where id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print(f'Flight with id = {id} not found')
        else:
            print(f'Flight with id = {id} deleted')
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)

    def search_row(self, id):
        row = None
        #id = int(input('Enter Id of the person to search: '))
        query = f'select * from flights where id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print(f'Flight with id = {id} not found')
        else:
            row = cursor.fetchone()
            print(f'Flight details are \n', str(row))
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return row

    def list_all_rows(self):
        query = 'select * from flights;'
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            count = cursor.execute(query)
            if count == 0:
                print(f'No rows found in the table')
            else:
                rows = cursor.fetchall()
                for row in rows:
                    print(str(row))
            cursor.close()
            self.disconnect_db(connection)
            return rows
        except:
            print('Error in reading rows')

    def get_latest_row_id(self):
        query = 'select max(id) from flights;'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        id = cursor.fetchone()
        cursor.close()
        self.disconnect_db(connection)
        return id[0]

oprs = Db_operations()
oprs.get_latest_row_id()