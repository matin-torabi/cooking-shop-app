from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
    
    def ready(self):
        from authentication.core.signals.register_signal import emit_user_registered
        from profiles.signals import profile
        