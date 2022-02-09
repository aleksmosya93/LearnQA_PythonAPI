import requests

method_list = [{"method": "GET"}, {"method": "POST"},
               {"method": "PUT"}, {"method": "DELETE"}]

print("GET:")
for method in method_list:
    response_get = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
    print(f"В метод GET передан параметр {method['method']}: " + response_get.text)
    if method['method'] == "GET":
        if 'success' in response_get.text:
            print("Методы совпадают, сервер тоже так считает. Все ОК\n")
        else:
            print("Методы совпадают, но сервер считает, что это не так\n")
    else:
        if 'success' in response_get.text:
            print("Методы не совпадают, но сервер считает, что все ОК\n")
        else:
            print("Методы не совпадают и сервер так считает. Все ОК\n")
print("\n")

print("POST:")
for method in method_list:
    response_post = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print(f"В метод POST передан параметр {method['method']}: " + response_post.text)
    if method['method'] == "POST":
        if 'success' in response_post.text:
            print("Методы совпадают, сервер тоже так считает. Все ОК\n")
        else:
            print("Методы совпадают, но сервер считает, что это не так\n")
    else:
        if 'success' in response_post.text:
            print("Методы не совпадают, но сервер считает, что все ОК\n")
        else:
            print("Методы не совпадают и сервер так считает. Все ОК\n")
print("\n")

print("PUT:")
for method in method_list:
    response_put = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print(f"В метод PUT передан параметр {method['method']}: " + response_put.text)
    if method['method'] == "PUT":
        if 'success' in response_put.text:
            print("Методы совпадают, сервер тоже так считает. Все ОК\n")
        else:
            print("Методы совпадают, но сервер считает, что это не так\n")
    else:
        if 'success' in response_put.text:
            print("Методы не совпадают, но сервер считает, что все ОК\n")
        else:
            print("Методы не совпадают и сервер так считает. Все ОК\n")
print("\n")

print("DELETE:")
for method in method_list:
    response_delete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print(f"В метод DELETE передан параметр {method['method']}: " + response_delete.text)
    if method['method'] == "DELETE":
        if 'success' in response_delete.text:
            print("Методы совпадают, сервер тоже так считает. Все ОК\n")
        else:
            print("Методы совпадают, но сервер считает, что это не так\n")
    else:
        if 'success' in response_delete.text:
            print("Методы не совпадают, но сервер считает, что все ОК\n")
        else:
            print("Методы не совпадают и сервер так считает. Все ОК\n")
print("\n")