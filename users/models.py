from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    date_of_birth = models.DateField(auto_now=False)
    gender = models.ForeignKey('Gender', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'users'

class Gender(models.Model):
    gender = models.CharField(max_length=50)

    class Meta:
        db_table = 'gender'