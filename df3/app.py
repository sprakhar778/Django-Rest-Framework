import requests
import json

URL = "http://127.0.0.1:8000/student/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    
    print(r.status_code)  # Print the status code to check if the request was successful
  
    try:
        data = r.json()  # Try to parse the response as JSON
        print(data)
        
    except ValueError:
        print("Response is not in JSON format")
        
# get_data()

import requests
import json

URL = "http://127.0.0.1:8000/student/"

def post_data():
    data = {
        
        'name': 'Rohan',
        'roll': 6,
        'city': 'Delhi',
    }
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}  # Add the Content-Type header
    r = requests.post(url=URL, data=json_data, headers=headers)
    
    print(r.status_code)  # Print the status code to check if the request was successful
  
    try:
        data = r.json()  # Try to parse the response as JSON
        print(data)
    except ValueError:
        print("Response is not in JSON format")

post_data()

