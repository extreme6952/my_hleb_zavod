from django.urls import path,include
from django.contrib.auth.views import LogoutView
from . import views

app_name = "account"

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('logged-out/',LogoutView.as_view(template_name='registration/loggedd_out.html'),
         name='logout'),
    path('registration/',views.UserRegistrationView.as_view(),name="user_registration"),
    path('profile-detail/',views.ProfileUserDetailView.as_view(),name='profile_worker')
]
