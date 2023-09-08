from django.contrib import admin
from django.urls import path, include
from gba_search.urls import urlpatterns as v1_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(v1_urls))
]
