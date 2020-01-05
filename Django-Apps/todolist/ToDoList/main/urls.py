from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('page2', views.page2, name='page2'),
    path('<int:id>', views.num, name='num'),
    path('<str:owner>', views.showlist, name='showlist'),
]