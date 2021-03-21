from .models import Texts
from django.forms import ModelForm, TextInput, Textarea


class TextsForm (ModelForm):
    class Meta:
        model = Texts  # Обращаемся к модели
        fields = ["title", "text"] # К этим полям. Надеюсь потом вспомню сюда ещё diff вписать
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите название",
            }),
            "text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Введите название",
            })
        }