# views
from panel.views.users import UsersPanellView
from django.urls import path



urlpatterns = [
    path('users/', UsersPanellView.as_view(), name='users'),

]
