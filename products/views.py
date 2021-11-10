import json

from django.http import JsonResponse
from django.views import View
from django.db.models import Avg

from .models import Product

class ProductView(View):
    def get(self, request, id):
        try:
            product         = Product.objects.get(id=id)
            average_rating  = round(product.review_set.aggregate(average = Avg("rating"))["average"],1)
            
            result = {
                "product_info" : {
                    "category"            : product.subcategory.category.name,
                    "sub_category"        : product.subcategory.name,
                    "name"                : product.name,
                    "author"              : product.author,
                    "publisher"           : product.publisher,
                    "date_published"      : product.date_published,
                    "price"               : product.price,
                    "description"         : product.description,
                    "index"               : product.index,
                    "thumbnail_image_url" : product.thumbnail_image_url,
                    "translator"          : product.translator,
                    "painter"             : product.painter,
                    "average_rating"      : average_rating if average_rating else 0
                },
                "review_info" :[{
                    "username"   : review.user.username,
                    "rating"     : review.rating,
                    "content"    : review.content,
                    "created_at" : review.created_at
                } for review in product.review_set.all()]
            }
            return JsonResponse({"message" : result}, status=200)
        
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "도서 정보가 없습니다."}, status=404)