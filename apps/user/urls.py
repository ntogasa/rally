from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.SignUpView, name='signup'),
    path('my_account/', views.DashboardView, name='account_dashboard'),
]