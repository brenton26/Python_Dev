from django.urls import include, path
from . import views

# URL Patterns - the first parameter is the pattern, the second is the method you're calling inside of your view
# Third is the name of the pattern/function.

urlpatterns = [
    path('', views.home, name='travel'),
    path('weather/', views.weather, name="weather"),
    ]
