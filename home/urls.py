from django.urls import path
from home.views import Home,AboutUs,ContactUs
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('aboutus/', AboutUs.as_view(), name='aboutus'),
    path('contactus/', ContactUs.as_view(), name='contactus'),
]