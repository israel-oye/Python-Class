import json

user_details = {
    'name': 'Segun',
    'job': 'Professional Doom Scroller',
    'is_employed': False 
}

json_str = json.dumps(user_details)
# print(json_str)

# Deserialization
string_from_js = '{"school":"AU College","location":"Osun","isElite":true}'
deserialized_obj = json.loads(string_from_js)
print(f"Data type: {type(deserialized_obj)}\nValue: {deserialized_obj}")
print(type(deserialized_obj['isElite']))