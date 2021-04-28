from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile
from .forms import RegistrationForm


class CustomUserAdmin(UserAdmin):

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'last_login',
        'date_joined',
        )

    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class UserProfileAdmin(admin.ModelAdmin):

    def thumbnail(self, object):

        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))

    thumbnail.short_description = 'Profile Picture'

    list_display = (
        'thumbnail',
        'user',
        'dates_of_birth',
        'phone_number',
        'address_line_1',
        'address_line_2',
        'postal_code',
        'city',
        'state',
        'country',
        )
    list_filter = ('user', 'phone_number', 'country',)
    fieldsets = (
        (None, {'classes': ('wide', 'extrapretty'),
                'fields': ('user', 'dates_of_birth')}),
        ('Contact Information', {'fields': (
            'phone_number',
            'address_line_1',
            'address_line_2',
            'postal_code',
            'city',
            'state',
            'country'
            )}),
        ('Media', {'fields': ('profile_picture',)}),
    )

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
