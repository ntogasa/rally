from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from .models import Expedition
from .forms import ExpeditionForm

# Create your views here.

class ExpeditionList(generic.ListView):
    # Retrieve all published blog post objects and order them
    queryset = Expedition.objects.filter()
    # Specify the template to populate and include in the response
    template_name = 'expedition/expedition_list.html'
    # Name the queried data, this key is used within the template to populate items
    context_object_name = 'expeditions'


def expedition_detail_view(request, pk, slug):
    """ This fnc provides the full page responses for each Expedition object
    :param pk           the 'pk' index associated with a specific expedition object in the database
    :param slug         the 'slug' associated with a specific expedition object in the database
    :return response    the appropriate response
    """
    # Retrieve a particular blog post object (from models.Post) specified by the provided slug parameter
    expedition = Expedition.objects.get(pk=pk, slug=slug)
    # The keys listed below are used by the template to dynamically retrieve data
    context = {'expedition': expedition}
    # return a response consisting of the request and a template filled with the context data
    return render(request, "expedition/expedition_detail.html", context=context)


def plan_expedition_view(request):
    form = ExpeditionForm(request.POST or None)

    # If the view receives a POST request...
    if request.method == "POST":
        # Check if form is valid
        if form.is_valid():
            # If valid, save input
            expedition = form.save(commit=False)
            # Save the plan creator as the leader of the expedition
            expedition.leader = request.user
            expedition.save()
        # Redirect user back to expedition list page
        return HttpResponseRedirect("/expedition")
    context = {'form': form}
    return render(request, 'expedition/plan_expedition.html', context)
