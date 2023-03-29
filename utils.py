# Make a function to return a flight when it has a certain id number
def search_flight(flight_id, flights):
    return [flight for flight in flights if flight['flight_id'] == flight_id]

# Write a function to get the index of the flight in the flight array where the id matches that which is in the argument
def get_index(flight_id, flights):
    for flight in flights:
        if flight['flight_id'] == flight_id:
            return flights.index(flight)

