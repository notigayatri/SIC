import flight_dao

class Flight_service:
    def __init__(self):
        self.oprs = flight_dao.Db_operations()

    def create_flight(self, flight_number, airline, departure, arrival):
        new_flight = flight_dao.Person(flight_number, airline, departure, arrival)
        return new_flight

    def delete_flight(self,id):
        self.oprs.delete_row(id)

    def update_flight(self):
        self.oprs.update_row()

    def search_flight(self,id):
        return self.oprs.search_row(id)

    def list_all_flights(self):
        return self.oprs.list_all_rows()
    
    def insert_flight(self,person):
        return self.oprs.insert_row(person)