from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# models
from authentication.models.custom_user import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    '''
    this is for user-customized model that is made with AbstractUser.
    '''
    
    # add your custom setting here
    pass
