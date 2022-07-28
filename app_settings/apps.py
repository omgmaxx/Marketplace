from django.apps import AppConfig

from .services.read_config import ReadConfig


class AppSettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_settings'

    def ready(self):
        ReadConfig()
