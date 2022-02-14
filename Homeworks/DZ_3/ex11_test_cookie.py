import requests

class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie = response.cookies
        print(cookie)
        cookie_value = cookie.get('HomeWork')

        assert "HomeWork" in cookie, f"В куки не приходит 'HomeWork'"
        assert cookie_value == "hw_value", f"В HomeWork приходит значение отличное от 'hm_value'"