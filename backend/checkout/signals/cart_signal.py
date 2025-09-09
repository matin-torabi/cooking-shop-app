
# django
from django.dispatch import receiver

# signal:
from authentication.core.signal import user_registered


# model:
from checkout.models.cart import Cart

"""
Signal to automatically create a profile for each new user.

Workflow:
    - Triggered when a user account is created.
    - Automatically creates and associates a profile with the new user.
"""

@receiver(user_registered)
def create_profile(sender, user, **kwargs):
    # Ensures a bascket is created only once, safe from race conditions
    Cart.objects.create(user=user)