'''
NOTE This is an add-on module for future model upgrades.

you can just import it like this:
    from authentication.models.status import UserStatus
    
and you can make a feild like this:
    status = models.CharField(max_length=10, choices=UserStatus.choices, default=UserStatus.PENDING)
    

'''
from django.db import models

class UserStatus(models.TextChoices):
    '''
        User account status:
        - PENDING: User just registered (awaiting admin approval).
        - CONFIRMED: Approved by admin.
        - BLOCKED: Account blocked for any reason.
    '''
    PENDING   = 'pending', 'Pending' 
    CONFIRMED = 'confirmed', 'Confirmed' 
    BLOCKED   = 'blocked', 'Blocked' 