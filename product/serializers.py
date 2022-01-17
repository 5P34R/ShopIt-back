from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from .models import Product

class ProductListSerializer(ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    
    def get_photo_url(self, product):
        request = self.context.get('request')
        photo_url = product.image.url
        return request.build_absolute_uri(photo_url)
    class Meta:
        model = Product
        fields = ['id','title', 'description', 'catagory', 'photo_url', 'price', 'discount', 'quantity', 'created_by', 'delivary_option']
    