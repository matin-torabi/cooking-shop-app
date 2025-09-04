# views
from authentication.views.register import FirstStepRegisterView, SecondStepRegisterView
from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path

urlpatterns = [
    # Registration endpoints
    path('register/step-one/', FirstStepRegisterView.as_view(), name='step-one-register'),
    path('register/step-two/', SecondStepRegisterView.as_view(), name='step-two-register'),
    

    # Token management
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
