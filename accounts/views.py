from django.shortcuts import render
from accounts.serializers import UserRegisterSerializer
from rest_framework.generics import CreateAPIView
from accounts.models import User


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer