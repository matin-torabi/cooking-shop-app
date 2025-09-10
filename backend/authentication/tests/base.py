from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from django.core.cache import cache


def get_test_token()-> str:
    User = get_user_model()
    user = User.objects.get_or_create(username='09999999999')
    token = AccessToken.for_user(user)
    return str(token)



class BaseApiTest(APITestCase):
     def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="09123456789")
        self.token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        cache.clear()