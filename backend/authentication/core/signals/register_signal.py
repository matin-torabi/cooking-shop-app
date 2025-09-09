"""
This file defines a signal handler that runs after a new user is created.

Workflow:
    1. Define your signal in a separate file (e.g., `signals.py`) or inside a dedicated folder (e.g., `signals/signal.py`) for cleaner code organization.

Example:

    # Django imports
    from django.dispatch import receiver

    # Custom signal
    from authentication.core.signal import user_registered

    # Your model
    from profiles.models import Profile

    @receiver(user_registered)
    def create_profile(sender, user, **kwargs):
        # Safely ensures that a Profile is created only once per user
        Profile.objects.get_or_create(user=user)

Configuration:
    In your app’s `apps.py`, register the signal by overriding the `ready` method:

        def ready(self):
            from profiles.signals import profile
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from authentication.core.signal import user_registered

User = get_user_model()

# After a user is created, a signal is triggered indicating that a new user has been registered.
@receiver(post_save, sender=User)
def emit_user_registered(sender, instance, created, **kwargs):
    if created:
        user_registered.send(sender=User, user=instance)