from django.urls import path
from user.api.register import UserRegisterView
from user.api.login import LoginView
from user.api.send import SendView
from user.api.showmessage import ShowMessage
urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/' , LoginView.as_view()),
    path('send/' , SendView.as_view()),
    path('messages/', ShowMessage.as_view())
]