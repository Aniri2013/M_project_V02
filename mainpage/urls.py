from django.contrib import admin
from django.urls import path, include
from mainpage.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('sing_in', sing_in),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
