from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.num, name='num'),
    path('<str:name>', views.showlist, name='showlist'),
]