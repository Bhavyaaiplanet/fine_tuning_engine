from django.urls import path
from .views import cloudSelect


urlpatterns = [
    path('' ,cloudSelect)
]
