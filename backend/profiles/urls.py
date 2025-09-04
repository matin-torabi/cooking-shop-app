
from profiles.views.navbar import NavbarView
from django.urls import path

urlpatterns = [
     path("navbar/", NavbarView.as_view(), name="navbar"),
]
