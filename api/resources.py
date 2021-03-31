
from tastypie.resources import ModelResource
from api.models import Product

class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'