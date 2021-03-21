from django.shortcuts import render, redirect
from .models import Texts
from .forms import TextsForm


def index(request):  # прост подгрузка html. html в свою очередь от шаблона base генериться
    texts = Texts.objects.all()
    return render(request, 'main/index.html', {'title': "Анализатор сложности", 'texts': texts})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == "POST":  # Гипотетически позволяет задать действие с вызовом POST
        form = TextsForm(request.POST)
        if form.is_valid():
            form.save()  # сохранка и редирект
            return redirect("home")
        else:
            error = 'Форма неверна'

    form = TextsForm()
    context = {
        "form": form,
        "error": error,
    }
    return render(request, 'main/create.html', context)
