from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ExpeditionsList.as_view, name='expeditions_list'),
    path('<int:pk>-<slug:slug>/', views.ExpeditionDetail.as_view, name='expedition'),
]