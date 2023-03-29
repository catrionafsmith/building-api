import requests
import json

# POST REQUEST

new_flight = {
    "from_city": "Edinburgh",
     "to_city": "Helsinki",
     "days": [1,  7],
     "captain": {'name': 'Ole',
                 'surname': 'Jonson'},
     "duration_min": 92,
     "capacity": 100,
     "booked": 10,
     "available": 90,
     "flight_id": 777
}

headers = {"content-type": "application/json"}
result = requests.post('http://127.0.0.1:8080/flights', headers=headers, data=json.dumps(new_flight))


# PUT REQUEST

updated_flight = {
    "new content": "test",
    "flight_id": 555
}
flight_id = 555
headers = {"content-type": "application/json"}
result = requests.put('http://127.0.0.1:8080/flights/{}'.format(flight_id), headers=headers, data=json.dumps(updated_flight))
# result = requests.put(f'http://127.0.0.1:8080/flights/{flight_id}', headers=headers, data=json.dumps(updated_flight))
print(result)

#  DELETE REQUEST
flight_id = 1818

headers = {"content-type": "application/json"}
result = requests.delete('http://127.0.0.1:8080/flights/{}'.format(flight_id), headers=headers)
print(result)