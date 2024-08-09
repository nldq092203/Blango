from blango_auth import views
import django.contrib.auth.urls
from django.urls import path, include

from django.contrib.auth import views as auth_views

urlpatterns = [
  # path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
  path("profile/", views.profile, name="profile"),
]