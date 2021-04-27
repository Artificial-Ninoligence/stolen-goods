from .views import HomeStoreView
from django.urls import path


app_name = 'store'

urlpatterns = [
    path('', HomeStoreView.as_view(), name='home'),
]
