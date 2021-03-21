from django.db import models


class Texts(models.Model):  # Классная штука этот импорт
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст')
    score = models.IntegerField('Оценка сложности', blank=True, null=True)  # blank и null не забыть убрать
    url = models.CharField('URL', blank=True, null=True, max_length=255)  # blank и null писать вместе.

    def __str__(self):
        return self.title

    class Meta:  # Это для красивого отображения
        verbose_name = "Текст"
        verbose_name_plural = "Тексты"
