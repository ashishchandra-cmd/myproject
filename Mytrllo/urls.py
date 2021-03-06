"""Mytrllo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from trlloapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index_view,name='index_view'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_signup/',views.user_signup,name='user_signup'),
    path('user_home/',views.user_home,name='user_home'),
    path('team_create/',views.team_create,name='team_create'),
    path('board_create/',views.board_create,name='board_create')

]
