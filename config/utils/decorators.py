from django.http import JsonResponse
import jwt


def jwt_required(view_func):
    def wrapper(request, *args, **kwargs):
        # Get the token from the Authorization header
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if auth_header is None or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Unauthorized"}, status=401)

        # Extract the token from the header
        token = auth_header.split(" ")[1]

        try:
            # Verify the token
            payload = jwt.decode(token, "secret_key", algorithms=["HS256"])

            # Attach the payload to the request
            request.user = payload

            # Call the view function
            return view_func(request, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)

    return wrapper
