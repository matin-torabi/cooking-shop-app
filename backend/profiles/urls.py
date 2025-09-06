# views:
from profiles.views.navbar import NavbarView
from profiles.views.complete_profile import CompleteProfileView
from profiles.views.save_profile_pic import UpdateProfileView
from profiles.views.delete_profile_pic import DeleteProfileView

from django.urls import path

urlpatterns = [
     path("navbar/", NavbarView.as_view(), name="navbar"),
     path("complete/", CompleteProfileView.as_view(), name="complete-profile"),
     path("update/", UpdateProfileView.as_view(), name="update-profile"),
     path("delete/", DeleteProfileView.as_view(), name="delete-profile"),
     
]
