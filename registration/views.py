from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from registration.forms import SignUpForm
from .forms import SignUpForm
from django.contrib.auth.models import User
# Create your views here.


from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'registration/dashboard.html'
    login_url = reverse_lazy('home')


