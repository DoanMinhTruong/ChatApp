from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers import LoginSerializer

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer.LoginSerializer
