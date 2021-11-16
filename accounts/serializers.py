from .models import *
from rest_framework import serializers
from .helper import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=  User
        fields= ['email','password','phone']

    def create(self, validated_data):
        user=User.objects.create(email=validated_data['email'],phone=validated_data['phone'])
        user.set_password(validated_data['password'])
        user.save()
        send_otp_mobile_number(user.phone,user)
        return user

