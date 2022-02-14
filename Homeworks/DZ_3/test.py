import requests

url = "https://playground.learnqa.ru/api/homework_header"

response = requests.get(url)

header = response.headers
print(header)