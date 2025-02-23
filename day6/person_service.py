import person_dao

class Person_service:
    def __init__(self):
        self.oprs = person_dao.Db_operations()

    def create_person(self, name, gender, dob, location):
        new_person = person_dao.Person(name, gender, dob, location)
        return new_person

    def delete_person(self,id):
        self.oprs.delete_row(id)

    def update_person(self):
        self.oprs.update_row()

    def search_person(self,id):
        return self.oprs.search_row(id)

    def list_all_persons(self):
        return self.oprs.list_all_rows()
    
    def insert_person(self,person):
        return self.oprs.insert_row(person)