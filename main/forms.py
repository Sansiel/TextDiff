from django.core.exceptions import ValidationError

from .models import Texts
from django.forms import ModelForm, TextInput, Textarea


class TextsForm (ModelForm):
    class Meta:
        model = Texts  # Обращаемся к модели
        fields = ["title", "text", "url"]  # К этим полям. Надеюсь потом вспомню сюда ещё diff вписать
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите название",
            }),
            "text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Введите текст",
            }),
            "url": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите url (Необзательно)",
            }),
        }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError('Slug may not be "Create"')
            return new_slug