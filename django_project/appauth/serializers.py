from rest_framework import serializers

from .models import (
    AppUser,
)


class AppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = (
            'id',
            'last_login',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'zip_code')


class AppUserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'})

    class Meta:
        fields = '__all__'
