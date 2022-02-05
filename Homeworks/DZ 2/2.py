import requests

method = {"method": "POST"}

response4 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
print(response4.text)