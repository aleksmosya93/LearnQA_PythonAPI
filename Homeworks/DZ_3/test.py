import requests

response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
cookie = response.cookies.get('HomeWork')
print(cookie)