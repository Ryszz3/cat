from django.contrib import admin
from django.urls import path

import products.views


app_name = "products"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products.views.index),
    path('search/', products.views.search, name='search')
]