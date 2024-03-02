from django.apps import AppConfig


class WsmandaderoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wsmandadero'

    def ready(self):
        from . import signals
