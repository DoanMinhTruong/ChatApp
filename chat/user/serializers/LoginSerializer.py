from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LoginSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': {
            'error_code': '400',
            'error_message': 'user không tồn tại',
            'data' : None
        }
    }   
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        del data['refresh'] , data['access']
        data['error_code'] = '0'
        data['error_message'] = 'success'
        data['data'] = {}

        # Add extra responses here
        data['data']['username'] = self.user.username        

        data['data']['token'] = {}
        data['data']['token']['refresh'] = str(refresh)
        data['data']['token']['access'] = str(refresh.access_token)
        return data