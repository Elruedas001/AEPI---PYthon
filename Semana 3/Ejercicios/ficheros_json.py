import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    json_filename = 'data.json'
    with open(json_filename, 'w') as file:
        json.dump(data, file, indent=4)
else:
    print(f"Ha habido un error en la peticion {response.status_code}")
