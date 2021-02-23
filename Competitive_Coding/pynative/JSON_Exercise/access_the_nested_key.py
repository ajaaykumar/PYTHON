# Question 5: Access the nested key ‘salary’ from the following JSON
import json

def extact_dict(dict_data):
    if isinstance(dict_data, dict):
        for key,value in dict_data.items():
            if key == "salary":
                yield dict_data[key]
            elif isinstance(value, dict):
                for result in extact_dict(value):
                    yield result

def access_key(sampleJson):
    data = json.loads(sampleJson)
    # print(data['company']['employee']['payble']['salary'])

    resp = extact_dict(data)
    print(list(resp)[0])

sampleJson = """{"company":{"employee":{"name":"emma","payble":{"salary":7000,"bonus":800}}}}"""
access_key(sampleJson)



