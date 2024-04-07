
# https://pynative.com/make-python-class-json-serializable/

import json
from json import JSONEncoder

class Employee:
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address

class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin

# subclass JSONEncoder
class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

def test_encoder():
    address = Address("Alpharetta", "7258 Spring Street", "30004")
    employee = Employee("John", 9000, address)

    print("Printing to check how it will look like:")
    print(EmployeeEncoder().encode(employee))

    print("Encode Employee Object into JSON formatted Data using custom JSONEncoder:")
    employeeJSONData = json.dumps(employee, indent=4, cls=EmployeeEncoder) #json object
    print(employeeJSONData)

    # Let's load it using the load method to check if we can decode it or not.
    print("Decode JSON formatted Data:")
    employeeJSON = json.loads(employeeJSONData) #python dict
    print(employeeJSON)

if __name__ == "__main__":
    test_encoder()
    
