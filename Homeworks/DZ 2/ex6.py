import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

len_list = response.history
last_response = response

print(len(len_list))
print(last_response.url)