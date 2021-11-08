import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Wedibooks.settings")
django.setup( )

from products.models import Menu, Category, Subcategory, Product

CSV_PATH_MENU = 'csv/menu.csv'
CSV_PATH_CATEGORY = 'csv/category.csv'
CSV_PATH_SUBCATEGORY = 'csv/subcategory.csv'
CSV_PATH_PRODUCT = 'csv/product.csv'

with open(CSV_PATH_MENU) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        menu_name = row[0]
        Menu.objects.create(name = menu_name)

with open(CSV_PATH_CATEGORY) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        category_name = row[0]
        category_menu = row[1]
        Category.objects.create(name = category_name, menu_id = category_menu)

with open(CSV_PATH_SUBCATEGORY) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        sub_category_name = row[0]
        sub_category_category = row[1]
        Subcategory.objects.create(name = sub_category_name, category_id = subcategory_category)

with open(CSV_PATH_PRODUCT) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        product_name = row[0]
        product_author = row[1]
        product_publisher = row[2]
        product_date_published = row[3]
        product_price = row[4]
        product_description = row[5]
        product_index = row[6]
        product_thumbnail_image_url = row[7]
        product_translator = row[8]
        product_painter = row[9]
        product_sub_category = row[10]
        Product.objects.create(
            name = product_name,
            author = product_author,
            publisher = product_publisher,
            date_published = product_date_published,
            price = product_price,
            description = product_description,
            index = product_index,
            thumbnail_image_url = product_thumbnail_image_url,
            translator = product_translator,
            painter = product_painter,
            sub_category_id = product_sub_category)