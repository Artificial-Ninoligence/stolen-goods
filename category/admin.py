from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['slug', 'name', 'created_at']
    list_filter = ['name', 'created_at']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)