from rest_framework import serializers
from user.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['sender' , 'receiver' , 'content']
