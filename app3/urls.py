from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
  
    path('test',views.test1fun,name='test'),
    path('login',views.loginfun,name='login'),
]
