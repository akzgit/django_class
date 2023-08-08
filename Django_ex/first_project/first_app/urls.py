from first_app import views
from django.urls import path,re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^$',views.index),
    path('admin/', admin.site.urls),
]
