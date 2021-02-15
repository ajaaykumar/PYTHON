# Question 1: Convert the following data into JSON format
import json

def convert_to_json(data):
    convJson = json.dumps(data, indent=4)
    print(convJson)
    print(type(convJson))

data = {"key1":"value1", "key2":"value2"}
convert_to_json(data)


