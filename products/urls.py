from .views import get_productos
from django.urls import path

urlpatterns = [
    path('', get_productos, name = "getProductos"),
]
