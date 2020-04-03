from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
import json
from .api_service import *
from .forms import *
from .serializers import *


# Home views
def home(request):
    return render(request, 'EdsApp/eds_home.html')

# Weather App view
def weather(request):
    if request.method == 'POST':
        user_input = request.POST.get('weather-search-string', None)
        location = get_queried_location(user_input)
        lat = location['latitude']
        lon = location['longitude']
        city = location['city']
        state = location['state']
        current_weather = get_current_weather(lat, lon)
        context = {
            'weather': current_weather,
            'city': city,
            'state': state,
        }
        return render(request, 'EdsApp/weather_app.html', context)
    else:
        location = get_user_location()
        lat = location['latitude']
        lon = location['longitude']
        city = location['city']
        state = location['state']
        current_weather = get_current_weather(lat, lon)
        context = {
            'weather': current_weather,
            'city': city,
            'state': state,
        }
        return render(request, 'EdsApp/weather_app.html', context)


def pet_form_choice(request):
    form = FormChoiceForm()
    if request.method == 'POST':
        choice = request.POST['form_choice']
        return render(request, 'EdsApp/animal_form.html', {'form': choice})
    return render(request, 'EdsApp/choose_animal_form.html', {'form': form})


def add_animal(request):
    print("--------------------")
    print("under add_animal")
    print("--------------------")
    print(request.POST.data)
    print("--------------------")
    if 'form_choice' in request.POST:
        print("--------------------")
        print("under add_animal")
        print("--------------------")
        print(request.POST)
        print("--------------------")
        if request.POST['form_choice'] == 'animal':
            form = AnimalForm(request.POST or None)
            print(form)
        elif request.POST['form_choice'] == 'dog':
            form = DogForm(request.POST or None)
            print(form)
        elif request.POST['form_choice'] == 'cat':
            form = CatForm(request.POST or None)
            print(form)
        elif request.POST['form_choice'] == 'dragon':
            form = DragonForm(request.POST or None)
            print(form)
        print("--------------------")
        print(form.is_valid())
        print("--------------------")
        print(form)
        print("--------------------")
        print(form.errors)
        print("--------------------")
        if form.is_valid():
            form.save()
            return redirect('animal_index')
        else:
            form = DogForm()
            return render(request, 'EdsApp/animal_form.html', {'form': form})
    else:
        form = FormChoiceForm()
        return render(request, 'EdsApp/animal_form.html', {'form': form})
            

def index(request):
    animals = Animal.animals.all()      
    context = {'animals': animals} 
    return render(request, 'EdsApp/animal_index.html', context)



# def guitarList(request):
#     get_guitars = Guitar.Guitars.all()      #Gets all the current jerseys from the database
#     context = {'guitars': get_guitars}      #Creates a dictionary object of all the jerseys for the template
#     return render(request, 'JimiJams/JimiJams_index.html', context)

# def add_guitar(request):
#     form = GuitarForm(request.POST or None)     #Gets the posted form, if one exists
#     if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
#         form.save()                             #Saves the valid form/jersey to the database
#         return redirect('guitar_index')                #Redirects to the index page, which is named 'jimiAdamin'
#     else:
#         print(form.errors)                      #Prints any errors for the posted form to the terminal
#         form = GuitarForm()                     #Creates a new blank form
#     return render(request, 'JimiJams/guitar_create.html', {'form':form})

# API Class views
class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = HelloSerializer

    @staticmethod
    def get(self):
        with open('EdsApp/static/EdsApp/cah.json', 'r') as rf:
            data = json.load(rf)
        an_api_view = data
        print(type(an_api_view))
        return Response({'message': 'Hello!', 'an_api_view': an_api_view})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (i.e. list, create)',
            'Automatically maps to URLS using routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create an item"""
        return Response({'created': 'item'})

    def retrieve(self, request, pk=None):
        """Retrieve an item"""
        return Response({'retrieve': 'item'})

    def update(self, request, pk=None):
        """Update an item"""
        return Response({'updated': 'item'})

    def partial_update(self, request, pk=None):
        """Update part of an item"""
        return Response({'partially_updated': 'item'})

    def destroy(self, request, pk=None):
        """Delete item"""
        return Response({'deleted': 'item'})






