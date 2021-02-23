# Question 7: Convert the following JSON into Vehicle Object
import json
class Vehicle():
    def __init__(self,name,engine,price):
        self.name = name
        self.engine = engine
        self.price = price

def vehicleDecoder(data):
    return Vehicle(data['name'], data['engine'], data['price'])
    
vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }', object_hook=vehicleDecoder)
print(vehicleObj.name)
print(vehicleObj.engine)
print(vehicleObj.price)



