import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text)

key = 'messages'
key2 = 'message'

if key2 in obj[key][1]:
    print(obj[key][1][key2])
else:
    print(f"Ключа {key2} нет в JSON")