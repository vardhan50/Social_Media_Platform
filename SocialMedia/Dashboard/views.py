# Dashboard/views.py
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Update the profile created by signal
            user.profile.twitter_handle = profile_form.cleaned_data['twitter_handle']
            user.profile.facebook_handle = profile_form.cleaned_data['facebook_handle']
            user.profile.save()

            login(request, user)
            return redirect('dashboard')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')
