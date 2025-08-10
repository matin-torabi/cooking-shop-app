from django.urls import reverse
from authentication.tests.base import BaseApiTest




class AuthTests(BaseApiTest):
    def setUp(self):
        super().setUp()
        self.step_one_register = reverse("step-one-register")
        self.step_two_register = reverse("step-two-register")

        self.step_one_login = reverse("step-one-login")
        self.step_two_login = reverse("step-two-login")
        
        self.phone = self.phone
        
    def register_one(self , value:str) -> str:
        return self.client.post(self.step_one_register, {"phone_number": value,})
        
    def login_one(self , value:str) -> str:
        return self.client.post(self.step_one_login, {"phone_number": value,})
        
    
        
    def register_two(self , value:str , otp , temp_token) -> str:
        return self.client.post(self.step_two_register, {"phone_number": value, 'otp_code':otp , 'temp_token':temp_token})
            
            
            
    def test_step_one_register(self):
        response = self.register_one(self.phone)
        self.assertEqual(response.status_code, 200)
    
        
    def test_step_one_register_empty(self):
        response = self.register_one('')
        self.assertEqual(response.status_code, 400)
        
    def test_step_one_register_invalid(self):
        response = self.register_one('invalid-number')
        self.assertEqual(response.status_code, 400)
        
    def test_step_two_register(self):
        response = self.register_one(self.phone)
        self.assertEqual(response.status_code, 200)

        otp = response.data.get("otp_code")
        temp_token =response.data.get('temp_token')
        response_two = self.register_two(self.phone , otp , temp_token)
        print(response_two.data)
        self.assertEqual(response_two.status_code, 201)
    
    #----------------------------------------------------------------------------
    
    def test_step_one_login(self):
        response = self.login_one(self.phone)
        print(response.data)
        self.assertEqual(response.status_code, 200)
    
    

