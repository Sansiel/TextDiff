from django.test import TestCase
from .models import Texts


class TextsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Texts.objects.create(title='Big', text='Bob')

    def test_title_label(self):  # Тестил как работает класс Meta
        texts = Texts.objects.get(id=1)
        field_label = texts._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название')

    def test_text_label(self):  # Проверял вывод данных
        texts = Texts.objects.get(id=1)
        field_label = texts.text
        self.assertEquals(field_label, 'Bob')

    def test_title_max_length(self):  # Тестил как работает ограничение длины
        texts = Texts.objects.get(id=1)
        max_length = texts._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)
