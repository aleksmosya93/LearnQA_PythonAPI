class TestShortPhrase:
    def test_short_phrase(self):
        phrase = input("Введите фразу: ")
        assert  len(phrase) < 15, f"Фраза '{phrase}' длиннее или равна 15 символам"