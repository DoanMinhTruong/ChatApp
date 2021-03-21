from rest_framework.views import APIView
import jwt 
from chat import settings
from user.models import Message,User
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from rest_framework import status
class ShowMessage(APIView):
    def post(self , request):
            try:
                data = jwt.decode(request.data['token'] ,  settings.SECRET_KEY,algorithms=["HS256"] )
            except:
                return JsonResponse({"message": "invalid token"} , status = status.HTTP_400_BAD_REQUEST)
            user_id = data['user_id']
            _with = User.objects.get(username = request.data['with'])
            messages = Message.objects.filter(sender = user_id , receiver = _with.id).values()
            return JsonResponse({"message" : list(messages)})