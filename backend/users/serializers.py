from rest_framework import serializers
from .models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone',
            'password',
            'password2',
        )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')

        user = CustomUser.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            phone=validated_data.get('phone', ''),
        )

        user.set_password(validated_data['password'])
        user.save()

        return user