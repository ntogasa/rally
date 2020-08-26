from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from social_django.models import UserSocialAuth


def home_view(request):
    """Handles requests for the home page."""
    return render(request, 'home.html')

@login_required
def settings_view(request):
    """Handles social media connection settings"""
    # recognize the user
    user = request.user
    # Check if user is logged into Facebook
    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None
    # User can disconnect if they have a password, or if they've connected another social media account
    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
    # Load the settings template with the correct user information
    return render(request, 'settings.html', {
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect,
    })

@login_required
def set_password_view(request):
    """Handles the setting up of account passwords"""
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm
    # If the request is a POST request...
    if request.method == 'POST':
        # Associate request with user and submit form input
        form = PasswordForm(request.user, request.POST)
        # If form is valid, save and update password
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated.')
            return redirect('set_password')
        # If form is not valid, ask for correction
        else:
            messages.error(request, 'Please correct the error below.')
    # If form is not a POST request, load a blank form associated with the user
    else:
        form = PasswordForm(request.user)
    return render(request, 'set_password.html', {'form': form})