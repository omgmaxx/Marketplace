from django.contrib import admin
from dynamic_preferences.admin import GlobalPreferenceAdmin
from dynamic_preferences.models import GlobalPreferenceModel

from app_settings.services.save_config import SaveConfig


class MeganoGlobalPreferenceAdmin(GlobalPreferenceAdmin):

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        SaveConfig()


admin.site.unregister(GlobalPreferenceModel)
admin.site.register(GlobalPreferenceModel, MeganoGlobalPreferenceAdmin)