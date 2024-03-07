from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from accounts.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = (
            "name",
            "last_name",
            "phone",
            "password",
        )


# pop methodu  = pop
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])

        user = User.objects.create(**validated_data)

        return user