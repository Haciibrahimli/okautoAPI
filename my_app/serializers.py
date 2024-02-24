from rest_framework import serializers
from my_app.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class BlogSeializer(serializers.ModelSerializer):
    class Meta:
        models = Blog
        fields = "__all__"

class ContactSrializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

