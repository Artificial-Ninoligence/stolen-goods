from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
# import debug_toolbar


urlpatterns = [

    # Admin login page
    path('stolen-goods-admin/', admin.site.urls),

    # Fake admin login page
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),

    # Debugging Tool UI
    # path('__debug__', include(debug_toolbar.urls)),

    # Home Page and all main pages
    path('', include('store.urls')),

    # Dashboard, Registration, Login, Logout
    path('accounts/', include('accounts.urls')),

    # Cart functionality
    path('cart/', include('carts.urls')),

    # Order and Payment (Paypal implementation)
    path('transactions/', include('transactions.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
