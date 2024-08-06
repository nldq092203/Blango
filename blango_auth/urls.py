from blango_auth import views
import django.contrib.auth.urls
from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm

urlpatterns = [
  path("", include("django.contrib.auth.urls")),
  path("", include("django_registration.backends.activation.urls")),
  path("profile/", views.profile, name="profile"),
  path(
    "accounts/register/",
    RegistrationView.as_view(form_class=BlangoRegistrationForm),
    name="django_registration_register",
  )
]