from django.db import models
from core.models import TimeStampModel

class User(TimeStampModel):
    username      = models.CharField(max_length=50)
    name          = models.CharField(max_length=50)
    email         = models.EmailField(unique=True)
    password      = models.CharField(max_length=200)
    year_of_birth = models.IntegerField()
    gender        = models.ForeignKey('Gender', on_delete=models.CASCADE)
    deleted_at    = models.DateTimeField(null=True)

    class Meta:
        db_table = 'users'

class Gender(models.Model):
    gender = models.CharField(max_length=50)

    class Meta:
        db_table = 'gender'