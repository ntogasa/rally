from django.shortcuts import render

# Create your views here.

def start_plan_view(request):
    return render(request, 'plan/start_plan.html')
