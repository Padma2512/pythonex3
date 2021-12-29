import requests

url="https://www.youtube.com/watch?v=x-RYqNxYIB8"

print(dir(requests))

response=requests.get(url=url)

print(response.status_code)

print(response.headers)

