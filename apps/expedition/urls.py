from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ExpeditionsList.as_view, name='expeditions_list')
]