from flask import Flask, jsonify, request
from flight_data import flights
from utils import search_flight, get_index

app = Flask(__name__)
#  Getting Information

@app.route('/')
def hello():
    return {"message": "You are welcome to XYZ Airline", "status": 200}

@app.route('/flights')
def get_flights():
    return jsonify(flights)

@app.route('/flights/<int:id>')
# def get_flight_by_id(id):
#     if search_flight(id, flights) == 1:
#         return jsonify.{"status": "No flights found with id"}
#     return search_flight(id, flights)
def get_flight_by_id(id):
    if search_flight(id, flights) == []:
        return jsonify({"Status": "No Flights found with ID {}".format(id)})
    return search_flight(id, flights)

# CREATE NEW FLIGHTS
@app.route('/flights', methods=["POST"])
def add_flight():
    flight = request.get_json()
    flights.append(flight)
    return jsonify(flight)

# UPDATE EXISTING FLIGHTS
@app.route('/flights/<int:id>', methods=["PUT"])
def update_flight(id):
    flight_to_update = request.get_json()
    index = get_index(id, flights)
    flights[index] = flight_to_update
    return jsonify(flights[index])

# DELETE AN EXISTING FLIGHT
@app.route('/flights/<int:id>', methods=["DELETE"])
def delete_flight(id):
    index = get_index(id, flights)
    deleted = flights.pop(index)
    return jsonify(deleted), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)