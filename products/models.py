from django.db import models
from core.models    import TimeStampModel

class Menu(models.Model):
    name = models.CharField(max_length=50)

    class Meta: 
        db_table = 'menus'

class Category(models.Model) : 
    name = models.CharField(max_length=50)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta: 
        db_table = 'categories'

class Subcategory(models.Model) :
    name     = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta: 
        db_table = 'subcategories'

class Product(models.Model) : 
    subcategory         = models.ForeignKey('Subcategory', on_delete=models.CASCADE)
    name                = models.CharField(max_length=500)
    author              = models.CharField(max_length=500)
    publisher           = models.CharField(max_length=100)
    date_published      = models.DateField()
    price               = models.DecimalField(max_digits=7, decimal_places=2)
    description         = models.TextField()
    index               = models.TextField(null=True)
    thumbnail_image_url = models.CharField(max_length=2000)
    translator          = models.CharField(max_length=100, null=True)
    painter             = models.CharField(max_length=100, null=True)
    head_description    = models.CharField(max_length=500, null=True)
    detail_description1 = models.CharField(max_length=500, null=True)
    detail_description2 = models.CharField(max_length=500, null=True)

    class Meta: 
        db_table = 'products'