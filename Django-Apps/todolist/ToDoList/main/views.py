from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(request):
    return HttpResponse("""
        <h1>Brenton is cool</h1>
        <h2>Look at my cool H2 tag</h2>
        <h4>Look at my cool H4 tag</h4>
    """)

def num(request, id):
    return HttpResponse(f'<h1>{id}</h1>')


def showlist(request, name):
    return HttpResponse(f'<h1>{ToDoList.objects.get(name=name)}</h1>')    