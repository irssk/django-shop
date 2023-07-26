from django.contrib import admin
from django.urls import path

from .views import home, section, category, product

urlpatterns = [
    path('', home),
    path('<slug:slug>', section, name="<slug>"),
    path('category/<slug:slug>', category, name="<slug>"),
    path('product/<slug:slug>', product, name="<slug>"),
]
