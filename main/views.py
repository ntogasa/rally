from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def home_view(request):
    """Handles requests for the home page."""
    return render(request, 'home.html')