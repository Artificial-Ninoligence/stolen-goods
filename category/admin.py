from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['slug', 'name', 'date_created']
    list_filter = ['name', 'date_created']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)