from django.contrib import admin

# models
from profiles.models.profile import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''
    this is for user Profiles
    '''
    # add your custom setting here
    pass

