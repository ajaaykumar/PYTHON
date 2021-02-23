# Question 3: PrettyPrint following JSON data
# PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").

import json

def pretty_json(data):
    # convJson = json.dumps(data, indent=2)
    # prettyJson = convJson.replace(":","=")
    # print(prettyJson)
    
    convJson = json.dumps(data, indent=4, separators=(",", "="))
    print(convJson)


sampleJson = {"key1": "value1", "key2": "value2"}
pretty_json(sampleJson)




