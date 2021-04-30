from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

from .textParse import TextToDiff


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


def gen_diff(s):
    td = TextToDiff.diff(s, None)
    return td

def gen_symbol(s):
    sym = TextToDiff.symb(s)
    return sym


class Texts(models.Model):  # Классная штука этот импорт
    title = models.CharField('Название', max_length=250)
    text = models.TextField('Текст')
    score = models.IntegerField('Оценка сложности', blank=True, null=True)  # blank и null не забыть убрать
    url = models.CharField('URL', blank=True, null=True, max_length=255)  # blank и null писать вместе.
    slug = models.SlugField(max_length=150, unique=True)
    symbol = models.IntegerField('Кол-во символов', blank=True, null=True)  #Добавлено по просьбе пользователей

    def get_absolute_url(self):
        return reverse('text_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
            self.score = gen_diff(self.text)
            self.symbol = gen_symbol(self.text)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:  # Это для красивого отображения
        verbose_name = "Текст"
        verbose_name_plural = "Тексты"


class Dictionary(models.Model):  # Словарь
    word = models.CharField('Слово', max_length=50)
    score = models.IntegerField('Оценка сложности')

    def __str__(self):
        return self.word

    class Meta:  # Это для красивого отображения
        verbose_name = "Словарь"
        verbose_name_plural = "Слова"
