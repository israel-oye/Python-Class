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
# print(json_str)

# with open('user.json', 'w') as file:
#     json.dump(user_details, file, indent=2)

# with open('file.json', 'w') as f:
#     json.dump(user_details, f, indent=1)

person = {
    'name': 'Pearson Jude',
    'height': 1.89,
    'nationality': 'British',
    'spouse': None,
    'hobbies': ('skiing', 'music'),
    'other_info': {
        'health': 'Not checked ❌',
        'insurance': 'Paid.'
    }
}

person_json_str = json.dumps(person, indent=2)
# print(person_json_str)


# # Deserialization
string_from_js = '{"school":"AU College","location":"Osun","isElite":true}'
# # Loads -> Decoding
deserialized_obj = json.loads(string_from_js)
# print(deserialized_obj)

# with open('package.json', 'r') as file:
#     package_dict = json.load(file)
#     print(type(package_dict))



# print(f"Data type: {type(deserialized_obj)}\nValue: {deserialized_obj}")
# print(type(deserialized_obj['isElite']))


person = {
    'name': 'Pearson Jude',
    'height': 1.89,
    'nationality': 'British',
    'spouse': None,
    'hobbies': ('skiing', 'music'),
    'other_info': {
        'health': 'Not checked ❌',
        'insurance': 'Paid.'
    }
}

# Serializing to a file
with open('person-data.json', 'w') as person_file:
    json.dump(person, person_file, indent=2)

# Deserializng the file
with open('person-data.json', 'r') as json_file:
    deserialized_person = json.load(json_file)
# print(deserialized_person)

print(deserialized_person['hobbies'][-1])

other_info: dict = deserialized_person['other_info']

# deserialized_person['other_info'].items()
for key in other_info:
    print(other_info[key].upper())

for key, value in other_info.items():
    print(value.upper())