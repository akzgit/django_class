from django.contrib import admin
from django.urls import path
from MongodbApp2 import views

urlpatterns = [
    path('add-book/', views.add_book, name='add_book'),
    
]
