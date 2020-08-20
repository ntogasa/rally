from django.shortcuts import render

def home_view(request):
    """Handles requests for the home page."""
    return render(request, 'home.html')
