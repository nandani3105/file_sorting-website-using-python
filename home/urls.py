from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sort_files/', views.sort_files, name='sort_files'),
]
