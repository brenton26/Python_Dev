from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('viewset', views.HelloViewSet, basename='viewset')

urlpatterns = [
    path('', views.home, name='eds_home'),
    path('', include(router.urls)),
    path('weather/', views.weather, name="weather"),
    path('pets/', views.pet_form_choice, name='pets'),
    path('pets/adopt/', views.add_animal, name='adopt'),
    path('pets/index/', views.index, name="animal_index"),
    path('api/', views.HelloAPIView.as_view(), name='api'),
    ]
