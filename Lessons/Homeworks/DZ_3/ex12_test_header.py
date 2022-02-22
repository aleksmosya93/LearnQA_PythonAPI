import requests

class TestHeader:
    def test_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"

        response = requests.get(url)

        header = response.headers
        print(header)

        header_value = response.headers.get('x-secret-homework-header')

        assert 'x-secret-homework-header' in response.headers, f"Заголовка 'x-secret-homework-header' нет в headers"
        assert header_value == "Some secret value", f"У заголовка 'x-secret-homework-header' значение не равно 'Some secret value'"