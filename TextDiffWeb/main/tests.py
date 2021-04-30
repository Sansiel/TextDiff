from django.test import TestCase
from .models import Texts
from .textParse import TextToDiff


class TextsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Texts.objects.create(title='Big Bob', text='One day I was liking creams')
        # Texts.objects.create(title='Big Bob', text='What are you doing?')

    def test_difficulty(self):  # Тест функции подсчёта сложности
        texts = Texts.objects.get(id=1)
        static_dict = {"i": 1,
                       "be": 2,
                       "one": 3,
                       "day": 4,
                       "like": 5,
                       "cream": 6}

        answer = TextToDiff.diff(texts.text, static_dict)
        # answer = TextToDiff.diff(texts.text, None)
        self.assertEquals(answer, float("58"))

    def test_difficulty_with_big_data(self):  # Тест функции подсчёта сложности BIG DATA
        inp = open('.//main//text.txt')
        string = ""
        for line in inp:
            string += str(line)
        answer = TextToDiff.diff(string, None)
        self.assertEquals(answer, float("75"))

    def test_parse_en(self):  # Тест функции определения языка
        texts = Texts.objects.get(id=1)
        answer = TextToDiff.parse(texts.text)
        self.assertEquals(answer, True)

    def test_parse_ru(self):  # Тест функции определения языка
        texts = "Привет"
        answer = TextToDiff.parse(texts)
        self.assertEquals(answer, False)

    def test_get_symbol_num(self):
        text="I'm the strongest hero, who beat big number of demons"
        answer = TextToDiff.symb(text)
        self.assertEquals(answer, int(42))

