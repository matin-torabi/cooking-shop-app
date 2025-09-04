from django.dispatch import receiver
from authentication.core.signal import user_registered
from profiles.models import Profile

@receiver(user_registered)
def create_profile(sender, user, **kwargs):
    Profile.objects.create(user=user)