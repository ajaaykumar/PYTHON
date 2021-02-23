# Question 6: Convert the following Vehicle Object into JSON
import json
# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price

#     def convert_toJson(self):
#         dic = {}
#         dic['name'] = self.name
#         dic['engine'] = self.engine
#         dic['price'] = self.price
#         json_data = json.dumps(dic,indent=4)
#         print(json_data)

# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
# vehicle.convert_toJson()

from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self,o):
        return o.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

vehicleJson = json.dumps(vehicle,indent=4,cls=VehicleEncoder)
print(vehicleJson)



