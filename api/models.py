from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    stock = models.IntegerField(default=0, null=True, blank=True)
    available = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return '%s - $%s' % (self.name, self.price)