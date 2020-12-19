from rest_framework import serializers
from generator.models import MasterProductsConfigurable


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterProductsConfigurable
        fields = ['model','sku','name','price','attribute_color']