from .models import CustomerUser, MerchantUser, UserProfile
from django.utils.html import format_html
from django.contrib import admin

class CustomerUserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_premium_account',
        'is_customer',
        'is_active',
        'date_joined',
        'last_login',
        )
    list_filter = ('email', 'first_name', 'is_premium_account', 'is_active')
    fieldsets = (
        (None, {'classes': ('wide', 'extrapretty'),
                'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_customer', 'is_premium_account',)}),
    )


class MerchantUserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_merchant',
        'is_active',
        'date_joined',
        'last_login',
        )
    list_filter = ('email', 'first_name', 'is_active')
    fieldsets = (
        (None, {'classes': ('wide', 'extrapretty'),
                'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'initial_name',)}),
        ('Permissions', {'fields': ('is_merchant',)}),
    )


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


admin.site.register(CustomerUser, CustomerUserAdmin)
admin.site.register(MerchantUser, MerchantUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)