import requests

method_list = [{"method": "GET"}, {"method": "POST"},
               {"method": "PUT"}, {"method": "DELETE"}]

for method in method_list:
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
        if
        print(response.text)
        print(response.status_code)