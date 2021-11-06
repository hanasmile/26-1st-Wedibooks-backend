import json

from django.http import JsonResponse
from django.views import View

from .models import Product

class ProductDetailView(View):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            result = []
            review_list = []
            reviews = product.review_set.all()
            for review in reviews:
                review_info = {
                    "username" : review.user.username,
                    "rating" : review.rating,
                    "content" : review.content,
                    "created_at" : review.created_at
                }
                review_list.append(review_info)

            info = {
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
                    "painter"             : product.painter
                    },
                "review_info" : review_list
            }
            
            result.append(info)

            return JsonResponse({"message" : result}, status=200)
        
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "도서 정보가 없습니다."}, status=401)