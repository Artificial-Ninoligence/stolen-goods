from django.contrib import admin
from .models import Victim


class VictimAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'occupation',
        'social_status',
        'date_modified',
        'date_created',
        )
    list_filter = ('name', 'date_modified', 'date_created',)
    fieldsets = (
        (None, {'classes': ('wide', 'extrapretty'),
                'fields': ('name', 'slug')}),
        ('Product Details', {'fields': (
            'occupation',
            'social_status',
            'address',
            )}),
    )

admin.site.register(Victim, VictimAdmin)
