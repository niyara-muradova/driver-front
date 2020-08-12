from django.urls import path
from settings_config import views


urlpatterns = [
    path('configs/', views.conf_choose, name='conf-choose'),
    path('devices/', views.devices, name='devices')
]