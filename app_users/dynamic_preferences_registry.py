from django.contrib.auth import get_user_model
from dynamic_preferences.forms import global_preference_form_builder
from dynamic_preferences.types import BooleanPreference, StringPreference
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.users.registries import user_preferences_registry

general = Section('general')
discussion = Section('discussion')


# global
@global_preferences_registry.register
class SiteTitle(StringPreference):
    section = general
    name = 'title'
    default = 'My site'
    required = False


@global_preferences_registry.register
class MaintenanceMode(BooleanPreference):
    name = 'maintenance_mode'
    default = False


# per-user
@user_preferences_registry.register
class CommentNotificationsEnabled(BooleanPreference):
    """Do you want to be notified on comment publication ?"""
    section = discussion
    name = 'comment_notifications_enabled'
    default = True


@user_preferences_registry.register
class PlaceHolder(StringPreference):
    name = 'place_holder'
    default = ''


# We instantiate a manager for our global preferences
global_preferences = global_preferences_registry.manager()

global_preferences['maintenance_mode'] = True
user = get_user_model().objects.get(username='Test_user')
