from django.contrib import admin
from django.urls import path, include
from mainpage.views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'mainpage'

urlpatterns = [
    path('sing_in', sing_in, name="sing_in"),
    path('registry', registry, name="registry"),
    path('cart', cart, name="cart"),
    path('checkout', checkout, name="checkout")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
