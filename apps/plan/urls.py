from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.start_plan_view, name='start_plan')
]