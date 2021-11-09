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

class Review(TimeStampModel):
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rating     = models.DecimalField(max_digits=2, decimal_places=1)
    content    = models.CharField(max_length=1000)

    class Meta:
        db_table = 'reviews'

class Cart(models.Model):
    user        = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product     = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity    = models.IntegerField()

    class Meta:
        db_table = 'cart'

class Order(TimeStampModel):
    user             = models.ForeignKey('users.User', on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=1000)
    contact          = models.CharField(max_length=120)
    product          = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount_paid      = models.IntegerField()
    order_number     = models.CharField(max_length=100)

    class Meta:
        db_table = 'orders'
        unique_together = ('user', 'product', 'order_number')

class Status(models.Model):
    order_status = models.CharField(max_length=100)