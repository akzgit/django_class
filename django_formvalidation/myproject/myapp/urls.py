from django.urls import path
from . import views


urlpatterns = [
    path('simple-form/',views.simple_form_view,name='simple-form'),
]
