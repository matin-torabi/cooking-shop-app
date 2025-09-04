from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.cache import cache
User = get_user_model()



class TestRegisterAPIView(APITestCase):
    def setUp(self):
        # URLs
        self.register_url = reverse('step-one-register')
        self.register_url_ = reverse('step-two-register')
        
        self.valid_phone = '09379196023'
        self.user_data = {'phone_number': self.valid_phone}
        
        cache.clear()

    def tearDown(self):
        cache.clear()

    def test_api_endpoint_success(self):
        """Test the API endpoint with valid data"""
        response = self.client.post(self.register_url, self.user_data, format='json')
        # after validations it send to second step register
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
        self.assertIn('temp_token', response.data)
        self.assertIn('status', response.data)
        
        
        # test auth/register/step-two/ , send otp and temp_token for validation
        request = self.client.post(self.register_url_ , response.data , format='json')

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertIn('refresh', request.data)
        self.assertIn('access', request.data)
        self.assertIn('status', request.data)
        self.assertIn('message', request.data)

    def test_api_endpoint_invalid_data(self):
        """Test the API endpoint with invalid data"""
        invalid_data = {'phone_number': 'invalid'}
        response = self.client.post(self.register_url, invalid_data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('message', response.data)
        
    def test_api_endpoint_invalid_data_12_digit(self):
        """Test the API endpoint with 12 digit number"""
        invalid_data = {'phone_number': '091111111112'}
        response = self.client.post(self.register_url, invalid_data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('message', response.data)
        
    def test_api_endpoint_empty_field(self):
        """Test the API endpoint with empty data"""
        invalid_data = {'phone_number': ''}
        response = self.client.post(self.register_url, invalid_data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        