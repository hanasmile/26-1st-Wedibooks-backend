from django.db import models
from core.models    import TimeStampModel

class Cart(models.Model):
    user        = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product     = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity    = models.IntegerField()

    class Meta:
        db_table = 'cart'

class Order(TimeStampModel):
    user             = models.ForeignKey('users.User', on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=1000)
    contact          = models.CharField(max_length=120)
    product          = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    amount_paid      = models.IntegerField()
    order_number     = models.CharField(max_length=100)

    class Meta:
        db_table = 'orders'
        unique_together = ('user', 'product', 'order_number')

class Status(models.Model):
    order_status = models.CharField(max_length=100)