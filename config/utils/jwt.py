import jwt
from datetime import datetime, timedelta
from django.http import JsonResponse
from .decorators import jwt_required


def generate_jwt(user):
    # Set the expiration time of the token
    exp_time = datetime.utcnow() + timedelta(days=1)

    # Define the payload of the token
    payload = {"user_id": user.id, "username": user.username, "exp": exp_time}

    # Generate the token
    token = jwt.encode(payload, "secret_key", algorithm="HS256")

    return token


@jwt_required
def protected_view(request):
    # Access the user's data from the request
    user_id = request.user.get("user_id")
    username = request.user.get("username")

    # Return a response with the user's data
    return JsonResponse({"user_id": user_id, "username": username})
