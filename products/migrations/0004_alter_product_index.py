# Generated by Django 3.2.8 on 2021-11-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211104_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='index',
            field=models.TextField(null=True),
        ),
    ]
