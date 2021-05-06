from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'image', 'date_created']
    list_filter = ['name', 'date_created']
    fieldsets = (
        (None, {'classes': ('wide', 'extrapretty'),
                'fields': ('name', 'slug', 'description', 'image')}),
    )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
