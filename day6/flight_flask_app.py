from flask import Flask, jsonify, request
import flight_service

flights = flight_service.Flight_service()

flights.oprs.create_table()
app = Flask(__name__)

@app.route('/flights',methods=['POST'])
def persons_create():
    body = request.get_json()
    new_flight = flights.create_flight(body['flight_number'], body['airline'], body['departure'], body['arrival'])
    print(type(new_flight))
    id = flights.insert_person(new_flight)
    flight = flights.search_person(id)
    flight_dict = {'id':flight[0], 'flight_number':flight[1], 'airline':flight[2], 'departure':flight[3], 'arrival': flight[4]}
    return jsonify(flight_dict)

@app.route('/flights/<id>',methods=['GET'])
def flights_read_by_id(id):
    flight = flights.search_flight(id)
    if flight == None:
        return jsonify("Flight not found")
    flight_dict = {'id':flight[0], 'flight_number':flight[1], 'airline':flight[2], 'departure':flight[3], 'arrival': flight[4]}
    return jsonify(flight_dict)

@app.route('/flights',methods=['GET'])
def flights_read_all():
    flights_list = flights.list_all_persons()
    flights_dict = []
    for flight in flights_list:
        flights_dict.append({'id':flight[0], 'flight_number':flight[1], 'airline':flight[2], 'departure':flight[3], 'arrival': flight[4]})
    return jsonify(flights_dict)

@app.route('/flights/<id>',methods=['PUT'])
def flights_update(id):
    body = request.get_json()
    old_flight_obj = flights.search_flight(id)
    if not old_flight_obj:
        return jsonify({'message': 'Flight not found'})
    new_flight_obj = []
    new_flight_obj.append(body['flight_number'])
    new_flight_obj.append(body['airline'])
    new_flight_obj.append(body['departure'])
    new_flight_obj.append(body['arrival'])
    new_flight_obj.append(id)
    new_flight_obj = tuple(new_flight_obj)
    flights.update_row(new_flight_obj)

    flight = flights.search_flight(id)
    flight_dict = {'id':flight[0], 'flight_number':flight[1], 'airline':flight[2], 'departure':flight[3], 'arrival': flight[4]}
    return jsonify(flight_dict)

@app.route('/flights/<id>',methods=['DELETE'])
def flights_delete(id):
    old_flight_obj = flights.search_flight(id)
    if not old_flight_obj:
        return jsonify({'message': 'Flight not found', 'is_error': 1})
    flights.delete_person(id)
    return jsonify({'message': 'Flight is deleted', 'is_error': 0})

app.run(debug=True)