import csv
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from .models import CSVUpload, Customer
from .serializers import CSVUploadSerializer,CustomerSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core import serializers
from rest_framework import serializers

class ViewAllCustomer(APIView):
    def get(self, request, format=None):   
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    
class CSVUploadView(APIView):
    
    parser_class = (FileUploadParser,)    
    serializer_class = CSVUploadSerializer
    User = get_user_model()

    def post(self, request):
        if not request.user.is_authenticated:
            token = request.META.get('authorization')
            if not token:
                token = request.COOKIES.get('token')
            if token:
                try:
                    user = User.objects.get(auth_token=token)
                except User.DoesNotExist:
                    return Response("User not found with the given token.", status=400)
                user = User.objects.get(auth_token=token)

        else:
            user = request.user
            
        file_serializer = CSVUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            file_obj = file_serializer.instance
            print(user)
            csv_upload = CSVUpload(file=file_obj.file, sender=user.id)
            csv_upload.save()
            
            with open(file_obj.file.path, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip the first row
                for row in reader:
                    email = row[0]
                    id = row[1]
                    
                    model_instance = Customer(id=id, email=email, sender=user.id)
                    model_instance.save()
            return Response(file_serializer.data, status=200)
        else:
            return Response(file_serializer.errors, status=400)