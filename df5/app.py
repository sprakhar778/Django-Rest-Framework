import requests
import json

URL = "http://127.0.0.1:8000/studentinfo/"

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
# get_data(1)

import requests
import json

URL = "http://127.0.0.1:8000/studentinfo/"

def post_data():
    data = {
        
        'name': 'Ravi',
        'roll': 201,
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


def update_data():
    data = {
        'id':2,
        'name': 'Ravi',
        'roll': 2,
        'city': 'Delhi',
    }
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}  # Add the Content-Type header
    r = requests.put(url=URL, data=json_data, headers=headers)
    
    print(r.status_code)  # Print the status code to check if the request was successful
  
    try:
        data = r.json()  # Try to parse the response as JSON
        print(data)
    except ValueError:
        print("Response is not in JSON format")

# update_data()


def delete_data(id):
   
    data = {'id': id}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    
    print(r.status_code)  # Print the status code to check if the request was successful
  
    try:
        data = r.json()  # Try to parse the response as JSON
        print(data)
        
    except ValueError:
        print("Response is not in JSON format")

# delete_data(2)