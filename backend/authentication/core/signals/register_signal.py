from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from authentication.core.signal import user_registered

User = get_user_model()

@receiver(post_save, sender=User)
def emit_user_registered(sender, instance, created, **kwargs):
    if created:
        user_registered.send(sender=User, user=instance)