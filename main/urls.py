from django.urls import path
from .views import cloudSelect,cloudConfig


urlpatterns = [
    path('' ,cloudSelect,name='cloud_select'),
    path('config/' , cloudConfig , name='cloud_config')
]
