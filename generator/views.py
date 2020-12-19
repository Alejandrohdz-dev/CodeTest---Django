from django.db.models import query
from rest_framework import generics, serializers
from django.shortcuts import render

from .models import MasterProductsConfigurable
from .serializers import ProductsSerializer


class ProductsListCreateAPIView(generics.ListCreateAPIView):
    """Provide a read-write view for products"""
    queryset = MasterProductsConfigurable.objects.all()
    serializer_class = ProductsSerializer
