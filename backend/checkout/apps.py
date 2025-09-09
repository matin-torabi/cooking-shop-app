from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'
    
    def ready(self):
        from authentication.core.signals.register_signal import emit_user_registered
        from checkout.signals.cart_signal import create_bascket

