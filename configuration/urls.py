from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('__debug__', include(debug_toolbar.urls)),
    #path('securelogin/', admin.site.urls),
    path('', include('store.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),

    # ORDERS
    path('transactions/', include('transactions.urls')),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
