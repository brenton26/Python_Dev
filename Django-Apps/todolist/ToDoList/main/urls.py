from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('page2/', views.page2, name='page2'),
    path('<int:id>', views.index, name='index'),
    # path('<str:owner>', views.showlist, name='showlist'),
    
]
