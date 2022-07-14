from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from app_users.models import Profile, UserMedia

admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


class ProfileUser(UserAdmin):
    list_display = ('username', 'get_name', 'email', 'is_active', 'get_group')
    inlines = (ProfileInline, )

    def get_name(self, obj):
        return f'{obj.first_name} {obj.profile.middle_name} {obj.last_name}'
    get_name.short_description = 'full name'

    def get_group(self, obj):
        if obj.is_superuser:
            return 'SuperUser'
        groups = [group_name[0] for group_name in obj.groups.all().values_list('name')]
        print(groups)
        if 'Admin' in groups:
            return 'Admin'
        elif 'Customer' in groups:
            return 'Customer'
        else:
            return 'Not verified'
    get_group.short_description = 'group'


admin.site.register(User, ProfileUser)


@admin.register(UserMedia)
class UserMediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploader')
    list_filter = ('uploader', )
