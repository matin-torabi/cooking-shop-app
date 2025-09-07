# views
from authentication.views.register import FirstStepRegisterView, SecondStepRegisterView
<<<<<<< HEAD
from authentication.views.login import FirstStepLoginView ,SecondSteploginView
=======
from authentication.views.login import FirstStepLoginView ,SecondStepLoginView
>>>>>>> d244423 (firs commit on linux)
from rest_framework_simplejwt.views import TokenRefreshView
from authentication.views.logout import LogoutView

from django.urls import path

urlpatterns = [
    # Registration endpoints
    path('register/step-one/', FirstStepRegisterView.as_view(), name='step-one-register'),
    path('register/step-two/', SecondStepRegisterView.as_view(), name='step-two-register'),
    
    # login endpoint
    path('login/step-one/', FirstStepLoginView.as_view(), name='step-one-login'),
<<<<<<< HEAD
    path('login/step-two/', SecondSteploginView.as_view(), name='step-two-login'),
    
    path('logout/', LogoutView.as_view(), name='logout'),
=======
    path('login/step-two/', SecondStepLoginView.as_view(), name='step-two-login'),
>>>>>>> d244423 (firs commit on linux)
    

    # Token management
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
