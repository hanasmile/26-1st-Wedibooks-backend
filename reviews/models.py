from django.db import models
from core.models    import TimeStampModel

class Review(TimeStampModel):
    product    = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rating     = models.DecimalField(max_digits=2, decimal_places=1)
    content    = models.CharField(max_length=1000)

    class Meta:
        db_table = 'reviews'