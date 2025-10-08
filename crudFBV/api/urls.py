from django.urls import path
from .views import home,list_and_create,retrive_modify

urlpatterns = [
    path('', home, name='home'),
    path('list_create/', list_and_create, name='list_create'),
    path('detail/<int:pk>/', retrive_modify, name='detail_modify'),
]