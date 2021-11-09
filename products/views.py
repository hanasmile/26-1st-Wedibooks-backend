import json

from django.http import JsonResponse
from django.views import View

from .models import Product
from django.db.models import Q, Avg, Count
# from django.db.models.functions import Round

class ProductView(View):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            reviews = product.review_set.all()
            result = {
                "product_info" : 
                {
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
                "review_info" :
                [
                    {
                    "username"   : review.user.username,
                    "rating"     : review.rating,
                    "content"    : review.content,
                    "created_at" : review.created_at
                    } for review in reviews
                ]
            }
            return JsonResponse({"message" : result}, status=200)
        
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "도서 정보가 없습니다."}, status=401)

class ProductListView(View): 
    def get(self, request):
        new_books = request.GET.get('new_books', None)
        sub_category = request.GET.get('sub_category', None)
        category = request.GET.get('category', None)
        rating = request.GET.get('rating', None)
        print(rating)
        q = Q()
       
        if sub_category:
            q &= Q(subcategory_id=sub_category)

        products = Product.objects.filter(q).annotate(reviews_count=Count('review')).annotate(average_rating=Avg('review__rating'))
        result=[]

        if rating:
            products=products.order_by(rating).reverse()[:20]

        if new_books:
            products=products.order_by('date_published').reverse()[:20]
        
        if category :
            q &= Q(subcategory__category_id=category)
            # products=products.values('name', 'author', 'thumbnail_image_url', 'date_published', 'rating').distinct()

        for product in products:
            result.append(
                {
                    "name" : product.name,
                    "author" : product.author,
                    "image" : product.thumbnail_image_url,
                    "date_published" : product.date_published,
                    "rating" : round(product.average_rating,1)
                    # [review.rating for review in Review.objects.filter(product_id = product.id)]
                }
            )
        return JsonResponse({"Products" : result}, status = 200)