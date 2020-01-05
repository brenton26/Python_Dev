from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def home(request):
    return render(request, 'main/base.html', {'name':'test'})


def page2(request):
    return render(request, 'main/home.html', {'name':'big hairy balls'})


def num(request, id):
    return HttpResponse(
        f'<h1>{id}</h1>'
        '<h1>Brenton is cool</h1>'
        '<h2>Look at my cool H2 tag</h2>'
        '<h4>Look at my cool H4 tag</h4>'
        )


def showlist(request, owner):
    ls = ToDoList.objects.get(owner=owner)
    return render(request, 'main/list.html', {'ls':ls})   