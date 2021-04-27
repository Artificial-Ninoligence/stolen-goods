from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__', include(debug_toolbar.urls)),
    path('', include('store.urls', namespace='store')),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
