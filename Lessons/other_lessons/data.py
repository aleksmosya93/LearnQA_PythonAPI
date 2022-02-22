import requests
from Lessons.environment import ENV_OBJECT

response = requests.post(f"{ENV_OBJECT.get_base_url()}/check_type", data={"param1": "value1"})
print(response.text)
print(response.url)