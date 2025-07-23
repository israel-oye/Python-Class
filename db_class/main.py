import sqlite3

connection = sqlite3.connect('db_class/users.sqlite3')

cursor = connection.cursor()

def create_table():
    create_query = 'CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, name TEXT, sex TEXT, age INTEGER)'

    global cursor
    cursor.execute(create_query)
    connection.commit()
    print('Created database...✅')

def insert_data(name: str, sex: str, age: int):
    insert_query = f'INSERT INTO Users (name, sex, age) VALUES (?, ?, ?)'

    global cursor
    cursor.execute(insert_query, (name, sex, age))
    connection.commit()
    print('Inserted values into database...✅')

def fetch_records_from_db():
    fetch_query = 'SELECT * FROM Users'
    
    cursor.execute(fetch_query)
    records = cursor.fetchall()
    connection.commit()

    return records

def delete_table():
    query = 'DROP TABLE Users'
    cursor.execute(query)
    connection.commit()

def fetch_users_from_json():
    import json

    with open('db_class/people.json', 'r') as file:
        data: dict = json.load(file)
    return data['people']


create_table()

people: list[dict[str]] = fetch_users_from_json()

for person in people:
    insert_data(
        name=person['name'],
        sex=person['sex'],
        age=person['age']
    )

print(fetch_records_from_db())

# insert_data('Eliora')
# delete_table()

connection.close()

# insert_data('Alice')
# insert_data('Bob')
# insert_data('Chukwuma')
# insert_data('Daphne')


