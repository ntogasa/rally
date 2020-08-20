from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def DashboardView(request):
    """Returns the user's account dashboard"""
    # Show the user's account dashboard page
    return render(request, "user/dashboard.html")


def SignUpView(response):
    """Handles the registration of new user via the sign up form"""
    # If the form is submitted (POST request)...
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        # Once submitted, redirect the user to the home page
        return redirect("/home")
    # If a blank form is asked for (GET request), such as when first loading the page...
    else:
        form = RegisterForm()
    # Load the sign up form page
    return render(response, "user/register.html", {"form": form})
