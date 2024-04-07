
# Python mapping with JSON
# Python	                JSON
# dict	                    object
# list, tuple	            array
# str	                    string
# int, long, float	        number
# True	                    true
# False	                    false
# None	                    null

import json 

# Convert from JSON to Python object
def json_to_python():
    print("--------- json_to_python ---------")
    # JSON string 
    employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
    print("This is JSON", type(employee)) 

    print("\nNow convert from JSON to Python") 

    # Convert string to Python dict 
    employee_dict = json.loads(employee) 
    print("Converted to Python", type(employee_dict)) 
    print(employee_dict) 


def python_to_json():
    print("--------- python_to_json ---------")
    # Python dict 
    employee_dict = {'id': '09', 'name': 'Nitin', 'department': 'Finance'} 
    print("This is Python", type(employee_dict)) 
    
    print("\nNow Convert from Python to JSON") 
    
    # Convert Python dict to JSON 
    json_object = json.dumps(employee_dict, indent=4) 
    print("Converted to JSON", type(json_object)) 
    print(json_object) 

def read_json_file():
    print("--------- read_json_file ---------")
    # Opening JSON file
    with open("sample.json", "r") as infile:
        # returns JSON object as
        # a dictionary
        data = json.load(infile)
        
        # Iterating through the json
        print("name: ", data["name"])


def save_json_file():
    print("--------- save_json_file ---------")
    # Data to be written
    dictionary ={
        "name" : "sathiyajith",
        "rollno" : 56,
        "cgpa" : 8.6,
        "phonenumber" : "9976770500"
    }
    
    with open("sample.json", "w") as outfile:
        json.dump(dictionary, outfile)

if __name__ == "__main__":
    json_to_python()
    python_to_json()
    save_json_file()
    read_json_file()
