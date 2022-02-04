import requests

print("---------HTTP-запрос любого типа без параметра method---------")
response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")

print(response1.text + "\n")

print("---------HTTP-запрос не из списка---------")
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", params={'method': 'HEAD'})

print(response2.text + "\n")

print("---------HTTP-запрос с правильным значением method---------")
response3 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': 'POST'})

print(response3.text + "\n")

print("---------HTTP-запрос---------")

params_list = ["get", "post", "put", "delete"]
method_list = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]

for i in method_list:
    for param in params_list:
        response4 = requests.i("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        if response4.starus_code == 200:
            print(f"method {i} with parameter params = {param} has following result {response4.result} with status code {response4.starus_code}")