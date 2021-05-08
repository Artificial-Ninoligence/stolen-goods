from django.contrib import admin
from .models import Product, ReviewRating, ProductGallery
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ReviewRatingAdmin(admin.ModelAdmin):

    list_display = ('subject', 'review', 'rating', 'status', 'ip_address', 'date_created', 'date_modified',)
    list_filter = ('subject', 'rating', 'date_modified', 'status', 'date_created',)
    fieldsets = (
        (None, {'classes': ('wide', 'extrapretty'),
                'fields': ('product', 'user',)}),
        ('Review and Rating Header', {'fields': ('subject', 'ip_address',)}),
        ('Review and Rating Details', {'fields': ('rating', 'review', 'status',)}),
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'discounted_price',
        'stock',
        'category',
        'is_available',
        'date_created',
        'date_updated'
        ]
    list_filter = ['is_available', 'date_created', 'stock', 'price']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {'classes': ('wide', 'extrapretty'),
                'fields': ('name', 'slug', 'category',)}),
        ('Display Image', {'fields': ('image',)}),
        ('Product Details', {'fields': ('stock', 'price', 'discounted_price', 'description', 'is_available',)}),
    )
    inlines = [ProductGalleryInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
admin.site.register(ProductGallery)
