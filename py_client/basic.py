import requests

url = 'http://localhost:8000/api/'

res = requests.get(url, params={'abc': 123}, json={'query': 'Hello world'})

#print(res.text)
#print(res.status_code)
print(res.json()['message'])