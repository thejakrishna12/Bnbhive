from django.urls import path
from .views import ProfileView
from django.contrib.auth import views as auth_views

from django.urls import reverse_lazy
urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    # path(
    #     'change-password/',
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='userprofile/changepassword.html',
    #         success_url = '/'
    #     ),
    #     name='change_password'
    # ),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='userprofile/changepassword.html',
            success_url = reverse_lazy('dashboard')), name='change-password'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='userprofile/password_reset_form.html',
             subject_template_name='userprofile/password_reset_subject.txt',
             email_template_name='userprofile/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='userprofile/password_reset_done.html'
         ),
         name='password_reset_done'),
     path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='userprofile/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='userprofile/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]