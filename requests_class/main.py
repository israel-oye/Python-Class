import requests

response = requests.get(' https://official-joke-api.appspot.com/random_joke')
# print(response.json())

details = {
    'name': 'Far rook',
    'game': 'Chess',
    'height': 1.75,
    'favorite_food': None,
}

r = requests.post('https://api.npoint.io/31f830e44de5e2783391', data=details)
print(r.json())
print(r.status_code)

# response_2 = requests.post('https://httpbin.org', data=details)
# print(response_2.text)
# print(response_2.status_code)