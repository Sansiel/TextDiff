from django.shortcuts import render, redirect
from .models import Texts
from .forms import TextsForm
from .textParse import TextToDiff


def index(request):  # прост подгрузка html. html в свою очередь от шаблона base генериться
    texts = Texts.objects.all()
    return render(request, 'main/index.html', {'title': "Анализатор сложности", 'texts': texts})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == "POST":  # Гипотетически позволяет задать действие с вызовом POST
        form = TextsForm(request.POST)
        form.errors
        if form.is_valid():
            form.save()  # сохранка и редирект
            return redirect("home")
        else:
            error = 'Форма неверна '+str(form.errors)

    form = TextsForm()
    context = {
        "form": form,
        "error": error,
    }
    return render(request, 'main/create.html', context)


def text_detail(request, slug):
    text = Texts.objects.get(slug__iexact=slug)
    return render(request, 'main/text_detail.html', {'text': text})
