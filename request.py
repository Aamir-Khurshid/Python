import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "aamir"
}
headers = {'Content-type': 'application/json;charset=UTF-8'}
response = requests.post(url, headers=headers, json=data)
print(response.text)