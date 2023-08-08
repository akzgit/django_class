"""
URL configuration for ProTwo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from AppTwo import views
from AppTwo.views import help
from AppTwo.views import UploadView
from AppTwo.views import student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apptwo/', include('AppTwo.urls')),
    path('AppTwo/empdetails.html',views.empdetails),
    path('help.html/', help, name='help'),
    path('upload/',UploadView.as_view()),
    path('form.html/',views.student_views),
]