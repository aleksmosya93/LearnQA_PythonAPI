import requests
import time
import json

create_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print("Шаг 1. Задача создана\n")

create_task_obj = json.loads(create_task.text)
token = create_task_obj["token"]
seconds = create_task_obj["seconds"]

get_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'token': token})
print("Шаг 2. Вызываем созданную задачу ДО того как задача готова")
get_task_obj = json.loads(get_task.text)
status_not_ready = get_task_obj["status"]
if status_not_ready == "Job is NOT ready":
    print(f"Status - {status_not_ready}\n")
else:
    print("Статус задачи не корректный\n")

print(f"Ждем {seconds} секунд(-ы)\n")
time.sleep(seconds)

get_task_2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'token': token})
print("Шаг 4. Вызываем созданную задачу повторно, после того как она стала готова")
get_task_2_obj = json.loads(get_task_2.text)
status_ready = get_task_2_obj['status']

if status_ready == 'Job is ready' and ('result' in get_task_2_obj):
    print(f"Status - {status_ready} and result available")
else:
    print("Status and result not correct")


