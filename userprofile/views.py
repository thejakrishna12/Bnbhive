from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .forms import ProfileForm
from django.contrib.auth.models import User

# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    # success_url = reverse_lazy('home')
    template_name = 'userprofile/profile.html'