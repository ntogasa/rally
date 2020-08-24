from django.shortcuts import render
from django.views import generic
from .models import Expedition

# Create your views here.
def plan_list_view(request):
    current_user = request.user
    plans_to_show = Expedition.objects.filter()