import requests

method = {"method": "GET"}

response4 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
print(response4.request)