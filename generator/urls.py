from django.urls import include, path
from .views import ProductsListCreateAPIView, CSVGenerator, csv_file_generator

urlpatterns = [
    path('', CSVGenerator.as_view(), name='home_page'),
    path('api/products/', ProductsListCreateAPIView.as_view(),name='products_list'),
    path('csv-file-generator', csv_file_generator, name='csv_file_generator'),
]
