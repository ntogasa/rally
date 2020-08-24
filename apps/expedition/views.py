from django.shortcuts import render
from django.views import generic
from .models import Expedition

# Create your views here.

class ExpeditionsList(generic.ListView):

    def get(self, request, *args, **kwargs):
        """Handle GET request and return response"""
        current_user = request.user
        queryset = Expedition.objects.get.all()


    def post(self, request, *args, **kwargs):
        """Handle POST request and return response"""
        current_user = request.user
        queryset = Expedition.objects.get.all()


class ExpeditionDetail(generic.DetailView):
    model = Expedition
    context_object_name = 'Expedition'
    template_name = 'expedition/expedition_detail.html'