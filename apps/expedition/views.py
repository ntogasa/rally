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



def expedition_detail_view(request, slug):
    """ This fnc provides the full page responses for each Expedition object
    :param slug         the 'slug' associated with a specific expedition object in the database
    :return response    the appropriate response
    """
    # Retrieve a particular blog post object (from models.Post) specified by the provided slug parameter
    expedition = Expedition.objects.get(slug=slug)
    # The keys listed below are used by the template to dynamically retrieve data
    context = {'expedition': expedition}
    # return a response consisting of the request and a template filled with the context data
    return render(request, "expedition/expedition_detail.html", context=context)
