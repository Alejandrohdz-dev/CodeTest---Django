import csv
from django.http import HttpResponse
from rest_framework import generics
from django.views.generic.base import TemplateView
# Local
from .models import MasterProductsConfigurable
from .serializers import ProductsSerializer


class ProductsListCreateAPIView(generics.ListCreateAPIView):
    """Provide a read-write view for products"""
    queryset = MasterProductsConfigurable.objects.all()
    serializer_class = ProductsSerializer


class CVSGenerator(TemplateView):
    """TemplateView for home page"""
    template_name = 'index.html'

def cvs_file_generator(request):
    """
    Function View to generate the CVS file from the database records, creating a new column with the
    sku and attribute_color attributes.
    """

    # Get all data from MasterProductsConfigurable Databse Table
    products = MasterProductsConfigurable.objects.raw('SELECT id,model,name,price,group_concat(concat, "|") AS configurations_variatons FROM (SELECT id,model,name,price, CASE WHEN attribute_color IS NULL THEN sku ELSE "sku=" || sku || "," || "color=" || attribute_color || "" END AS concat FROM master_products_configurable) GROUP BY model')

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_database_write.csv"'

    writer = csv.writer(response)
    writer.writerow(['Model', 'Name', 'Price', 'Configurations_variatons'])

    for product in products:
        writer.writerow([product.model, product.name, product.price, product.configurations_variatons])

    return response