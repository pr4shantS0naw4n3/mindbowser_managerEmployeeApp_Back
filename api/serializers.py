from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from .models import Manager,Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('id','firstName','lastName','email','phone_number','manager')

class ManagerSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        fields=('name','email','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        return Manager.objects.create_user(**validated_data)


JWT_PAYLOAD_HANDLER= api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class ManagerLoginSerializer(serializers.Serializer):
    email=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=255,write_only=True)
    token=serializers.CharField(max_length=255,read_only=True)

    def validate(self, data):
        email=data.get("email",None)
        password=data.get("password",None)
        user=authenticate(email=email,password=password)
        print("USERR:",user)
        if user is None:
            raise serializers.ValidationError(
                'Invalid Credentials'
            )

        try:
            payload=JWT_PAYLOAD_HANDLER(user)
            jwt_token=JWT_ENCODE_HANDLER(payload)
            update_last_login(None,user)
        except:
            raise serializers.ValidationError(
                'User with this email and password is not found.'
            )

        return{
            'email':user.email,
            'token':jwt_token
        }
