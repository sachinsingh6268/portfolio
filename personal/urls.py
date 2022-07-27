from django.contrib import admin
from django.urls import path, include
from personal import views

urlpatterns = [
    path('', views.index)
]
