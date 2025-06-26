import json

user_details = {
    1: 101,
    'name': 'Segun',
    'job': 'Professional Doom Scroller',
    'is_employed': False,
    'friends': ['Shaul', 'Yitzchak', 'Shimeon', 'Yochanan']
}

# Dumps -> Encoding
json_str = json.dumps(user_details, indent=1)
print(json_str)

with open('user.json', 'w') as file:
    json.dump(user_details, file, indent=2)




# Deserialization
string_from_js = '{"school":"AU College","location":"Osun","isElite":true}'
# Loads -> Decoding
deserialized_obj = json.loads(string_from_js)
print(f"Data type: {type(deserialized_obj)}\nValue: {deserialized_obj}")
print(type(deserialized_obj['isElite']))