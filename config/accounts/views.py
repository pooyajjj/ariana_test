from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from utils.jwt import generate_jwt
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# def login(request):
#     # Get the username and password from the request
#     username = request.POST.get('username')
#     password = request.POST.get('password')

#     # Authenticate the user
#     user = authenticate(request, username=username, password=password)

#     if user is not None:
#         # Generate a JWT token for the user
#         token = generate_jwt(user)

#         # Return the token in a JSON response
#         return JsonResponse({'token': token})
#     else:
#         # Return an error message
#         return JsonResponse({'error': 'Invalid credentials'})