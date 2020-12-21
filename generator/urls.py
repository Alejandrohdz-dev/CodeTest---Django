from django.urls import include, path
from .views import ProductsListCreateAPIView, CVSGenerator, cvs_file_generator

urlpatterns = [
    path('', CVSGenerator.as_view(), name='home_page'),
    path("api/products/", ProductsListCreateAPIView.as_view(),name="products_list"),
    path('cvs-file-generator', cvs_file_generator, name='csv_file_generator'),
]