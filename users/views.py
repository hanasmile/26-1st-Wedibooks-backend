import json, re, bcrypt, jwt

from django.http import JsonResponse
from django.views import View
from django.conf import settings

from .models import User, Gender

class SignupView(View):
    def post(self, request):
        try:
            data          = json.loads(request.body)
            username      = data['id']
            name          = data['name']
            password      = data['password']
            email         = data['email']
            year_of_birth = data['yearOfBirth']
            gender        = data['gender']
            
            if not re.match('^[A-Za-z]{1}[A-Za-z0-9]{3,}$', username):
                return JsonResponse({"message": "Id format is not valid"}, status=400)

            if not re.match('^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*-+_=?]).{8,}$', password):
                return JsonResponse({"message": "Password_Validation_Error"}, status=400)

            if not re.match('^[\w+-]+@[\w]+\.[\w.]+$', email):
                return JsonResponse({"message": "Email format is not valid"}, status=400)

            if User.objects.filter(username = username).exists():
                return JsonResponse({"message": "ID_Exist_Error"}, status=400)

            if User.objects.filter(email = email).exists():
                return JsonResponse({"message": "Email_Exist_Error"}, status=400)
            
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            User.objects.create(
                username      = username,
                name          = name,
                password      = hashed_password.decode('utf-8'),
                email         = email,
                year_of_birth = year_of_birth,
                gender        = Gender.objects.get(id = gender)
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "Key_Error"}, status=400)

class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data['id']
            password = data['password']
            user = User.objects.get(username=username)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message": "INVALID_USER"}, status=401)
                
            access_token = jwt.encode({"user_id": user.id}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
            return JsonResponse({"access_token": access_token}, status=200)
            
        except KeyError:
            return JsonResponse({"message": "Key_Error"}, status=400)
            
        except User.DoesNotExist:
            return JsonResponse({"message": "Does_Not_Exist"}, status=404)