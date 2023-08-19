from django.urls import path
from . import views

urlpatterns = [
    path('',views.book_list,name='book_list'),
    path('details/<int:pk>/',views.book_details,name='book_details'),
    path('update/<int:pk>/',views.book_update,name='book_update'),
    path('delete/<int:pk>/',views.book_delete,name='book_delete'),
    path('create/',views.book_create,name='book_create'),
]
