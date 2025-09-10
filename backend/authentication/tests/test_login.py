# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from django.core.cache import cache
# User = get_user_model()



# class TestLoginAPIView(APITestCase):
#     def setUp(self):
#         # URLs
#         self.login_step_one = reverse('step-one-login')
#         self.login_step_two = reverse('step-two-login')
        
#         self.user_data = {'phone_number': '09999999999'}
        
#         cache.clear()

#     def tearDown(self):
#         cache.clear()

#     def test_login_step_one(self):
#         """Test the API endpoint with valid data"""
#         response = self.client.post(self.login_step_one, self.user_data, format='json')
#         # after validations it send to second step login
#         print(response.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('message', response.data)
#         self.assertIn('temp_token', response.data)
#         self.assertIn('status', response.data)
        
        
#         # test auth/login/step-two/ , send otp and temp_token for validation
#         # request = self.client.post(self.login_url_ , response.data , format='json')

#         # self.assertEqual(request.status_code, status.HTTP_201_CREATED)
#         # self.assertIn('refresh', request.data)
#         # self.assertIn('access', request.data)
#         # self.assertIn('status', request.data)
#         # self.assertIn('message', request.data)

#     # def test_api_endpoint_invalid_data(self):
#     #     """Test the API endpoint with invalid data"""
#     #     invalid_data = {'phone_number': 'invalid'}
#     #     response = self.client.post(self.login_url, invalid_data, format='json')
#     #     # print(response.data)
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     self.assertIn('message', response.data)
        
#     # def test_api_endpoint_invalid_data_12_digit(self):
#     #     """Test the API endpoint with 12 digit number"""
#     #     invalid_data = {'phone_number': '091111111112'}
#     #     response = self.client.post(self.login_url, invalid_data, format='json')
#     #     # print(response.data)
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     #     self.assertIn('message', response.data)
        
#     # def test_api_endpoint_empty_field(self):
#     #     """Test the API endpoint with empty data"""
#     #     invalid_data = {'phone_number': ''}
#     #     response = self.client.post(self.login_url, invalid_data, format='json')
#     #     # print(response.data)
#     #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        