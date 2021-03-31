from django.contrib import admin

# Register your models here.

from .models import Product

class ProductModelAdmin(admin.ModelAdmin):

    list_display = ["name","price","stock","available","created_at"]
    list_editable = ["price","stock","available"]
    list_filter = ["name","price","available"]

    class Meta:
        model = Product

admin.site.register(Product, ProductModelAdmin)