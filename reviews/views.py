import json

from django.http import JsonResponse
from django.views import View

from users.utils import login_required
from .models import Review

class ReviewView(View):
    @login_required
    def post(self,request):
        try:
            data    = json.loads(request.body)
            product = data['product']
            rating  = data['rating']
            content = data['content']
            
            Review.objects.create(
                user_id    = request.user.id,
                product_id = product,
                rating     = rating,
                content    = content
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "Key_Error"}, status=400)