from django.dispatch import receiver
from authentication.core.signal import user_registered
from checkout.models.cart import Cart

@receiver(user_registered)
def create_bascket(sender, user, **kwargs):
    Cart.objects.get_or_create(user=user)