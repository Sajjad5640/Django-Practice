from django.db import models

# Create your models here.

class ProductModel(models.Model):
    PRODUCT_CATEGORY =[
        ('Electric','Electric'),
        ('Cloth','Cloth'),
        ('Food','Food'),
    ]

    name = models.CharField(max_length=200, null=True)
    product_type = models.CharField(choices=PRODUCT_CATEGORY, max_length=20, null=True)
    product_price = models.FloatField(null=True)
    description = models.TextField(null=True)
    qty =models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to='media/product_image',null=True,blank=True)

    def __str__(self):
        return self.name