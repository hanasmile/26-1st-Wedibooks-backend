import json, re, bcrypt, jwt

from django.http import JsonResponse
from django.conf import settings
from .models import User

def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get("Authorization")
            payload      = jwt.decode(access_token, settings.SECRET_KEY, settings.ALGORITHM)
            user         = User.objects.get(id = payload['user_id'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status = 400)
            
        except User.DoesNotExist:
            return JsonResponse({"message": "ID_Does_Not_Exist_Error"}, status=404)
        
        return func(self, request, *args, **kwargs)
    return wrapper