from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ExpeditionList.as_view(), name='expeditions_list'),
    path('<int:pk>-<slug:slug>/', views.expedition_detail_view, name='expedition'),
    path('plan_a_trip/', views.plan_expedition_view, name='plan_expedition'),
]