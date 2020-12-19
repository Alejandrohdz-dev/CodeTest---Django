from django.urls import include, path
from .views import ProductsListCreateAPIView

urlpatterns = [
    path("api/products/", ProductsListCreateAPIView.as_view(),name="products-list"),
]