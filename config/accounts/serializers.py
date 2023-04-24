from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"], email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ("username", "email", "password", "is_active")
