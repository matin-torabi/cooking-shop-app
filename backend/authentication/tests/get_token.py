
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken



def get_test_token()-> str:
    User = get_user_model()
    
    user = User.objects.get_or_create(username='09999999999')
    token = AccessToken.for_user(user)
    return str(token)