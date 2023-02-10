from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class Home(TemplateView):
    template_name = 'index.html'

class AboutUs(TemplateView):
    template_name = 'about.html'

class ContactUs(TemplateView):
    template_name = 'contact.html'