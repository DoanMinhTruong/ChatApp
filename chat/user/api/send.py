from rest_framework.views import APIView
from user.serializers.LoginSerializer import LoginSerializer
from django.http import JsonResponse
import jwt
from chat import settings
from rest_framework import status
from user.models import User
from user.serializers import MessageSerializer
class SendView(APIView):
    def post(self, request):
        try:
            data = jwt.decode(request.data['token'] ,  settings.SECRET_KEY,algorithms=["HS256"] )
            user_id = data['user_id']
            user = User.objects.get(pk = user_id)
            receiver = User.objects.get(username = request.data['receiver'])
            obj = {
            'sender' : user_id,
            'receiver' : receiver.id,
            'content' : request.data['content']
            }
            serializer = MessageSerializer.MessageSerializer(data = obj)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse({'status': 'ok'}, status = status.HTTP_200_OK)
        except:
            return JsonResponse({"status" : "error"} , status  = status.HTTP_400_BAD_REQUEST)
        
        
    