
# django
from django.dispatch import receiver

# signal:
from authentication.core.signal import user_registered


# model:
from profiles.models import Profile

"""
Signal to automatically create a profile for each new user.

Workflow:
    - Triggered when a user account is created.
    - Automatically creates and associates a profile with the new user.
"""

@receiver(user_registered)
def create_profile(sender, user, **kwargs):
    # Ensures a Profile is created only once, safe from race conditions
    Profile.objects.get_or_create(user=user)
