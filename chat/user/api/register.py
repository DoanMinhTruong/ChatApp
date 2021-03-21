from rest_framework.views import APIView

from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from user.serializers import UserSerializer
from rest_framework import status
class UserRegisterView(APIView):
    def post(self ,request):
        serializer = UserSerializer.UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user =  serializer.save()
            return JsonResponse(
                {'message': 'Register Successfull'}
            ,status = status.HTTP_201_CREATED)
        return JsonResponse(
                {'message': 'Register Unsuccessfull'}
            ,status = status.HTTP_400_BAD_REQUEST)
