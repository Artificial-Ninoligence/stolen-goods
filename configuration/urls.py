from django.contrib import admin
from django.urls import path
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
]
