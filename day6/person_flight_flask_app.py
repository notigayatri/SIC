from flask import Flask, jsonify, request

import person_dao
persons=person_dao.Db_operations()


persons.create_table()

app = Flask(__name__)

@app.route('/person',methods=['POST'])
def persons_create():
    body = request.get_json()
    new_person = person_dao.Person(body['name'], body['gender'], body['dob'], body['location'])
    id = persons.insert_row(new_person)
    person= persons.search_row(id)
    person_dict = {'id':person.id, 'name':person.name, 'gender':person.gender, 'dob':person.dob, 'location': person.location}
    return jsonify(person_dict)

@app.route('/new_person/<id>',methods=['GET'])
def person_read_by_id(id):
    person = persons.search_row(id)
    print(person)
    print(type(person))
    if person == None:
        return jsonify("person not found")
    person_dict = {'id':person.id, 'name':person.name, 'gender':person.gender, 'dob':person.dob, 'location': person.dob}
    return jsonify(person_dict)

@app.route('/flights',methods=['GET'])
def persons_read_all():
    persons_list = persons.list_all_rows()
    person_dict = []
    for person in persons_list:
        person_dict.append({'id':person.id, 'name':person.name, 'gender':person.dob, 'dob':person.dob, 'location': person.dob})
    return jsonify(person_dict)

@app.route('/person/<id>',methods=['PUT'])
def persons_update(id):
    body = request.get_json()
    old_person = persons.search_row(id)
    if not old_person:
        return jsonify({'message': 'Person not found'})
    old_person.name = body['name']
    old_person.gender = body['gender']
    old_person.dob = body['dob']
    old_person.location = body['location']
    id = body['id']
    persons.update_row(old_person, id)
    person = persons.search_row(id)
    person_dict = {'id':person.id, 'name':person.name, 'gender':person.dob, 'dob':person.dob, 'location': person.dob}
    return jsonify(person_dict)

@app.route('/person/<id>',methods=['DELETE'])
def persons_delete(id):
    old_person = persons.search_row(id)
    if not old_person:
        return jsonify({'message': 'Person not found', 'is_error': 1})
    persons.delete_row(id)
    return jsonify({'message': 'Person is deleted', 'is_error': 0})

app.run(debug=True)