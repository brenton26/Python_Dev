from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateNewList
from .models import Item, ToDoList


# Create your views here.
def home(request):
    return render(request, 'main/base.html', {'name':'test'})


def page2(request):
    return render(request, 'main/home.html', {'name':'big hairy balls'})


# def num(request, id):
#     return HttpResponse(
#         f'<h1>{id}</h1>'
#         '<h1>Brenton is cool</h1>'
#         '<h2>Look at my cool H2 tag</h2>'
#         '<h4>Look at my cool H4 tag</h4>')


# def showlist(request, owner):
#     ls = ToDoList.objects.get(owner=owner)
#     if request.method == 'POST':
#         pass
#     return render(request, 'main/list.html', {'ls':ls})   


def index(request, id):
    ls = ToDoList.objects.get(id=id)

    # {'save':['save'], 'c1':['clicked']}
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('save'):
            for item in ls.item_set.all():
                if request.POST.get('c' + str(item.id)) == 'clicked':
                    item.complete = True
                else:
                    item.complete = False

                item.save()
        elif request.POST.get('new_item'):
            txt = request.POST.get('new')
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid!")

    elif request.POST == 'GET':
        pass

    return render(request, 'main/list.html', {'ls':ls})


def create(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect('/%i' %t.id)

    else:
        form = CreateNewList()
    return render(request, 'main/create.html', {'form': form})
