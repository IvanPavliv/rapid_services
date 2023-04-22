from django.contrib import admin
from django.urls import path, re_path
from timezones.views import TimeZoneAPIView 

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^timezone/[^0-9]+', TimeZoneAPIView.as_view(), name='timezone'),
]
