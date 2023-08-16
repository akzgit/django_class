from django.contrib import admin
from django.urls import path, include
from . views import contactview,successview

urlpatterns=[
    path("contact/",contactview,name="contact"),
    path("success/",successview,name="success"),
]