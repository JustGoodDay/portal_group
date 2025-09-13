"""
URL configuration for core project.

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
from django.urls import path
from authentication_app.views import *
from forum_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
# Форум
    path('forum/', forum_list, name='forum_list'),
    path('forum/new/', forum_create, name='forum_create'),
# Жалобы
    path('complaints/', complaint_list, name='complaint_list'),
    path('complaints/new/', complaint_create, name='complaint_create'),
]

