from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import HttpResponse


class RegisterView(APIView):
    serializer_class = UserRegistrationSerializer
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"username": user.username, "email": user.email})
        else:
            return Response(serializer.errors)



class ObtainTokenView(APIView):
    serializer_class = UserRegistrationSerializer
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            response = Response({"token": token.key})
            response.set_cookie('token', token.key, httponly=True)
            return response
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)