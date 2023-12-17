from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField()
    sender = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
    ]

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"id:{self.id}, email: {self.email}, sender: {self.sender}, created_at: {self.created_at}"
    

class CSVUpload(models.Model):
    file = models.FileField(upload_to='csvs/')
    # sender = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=50)

    uploaded_at = models.DateTimeField(auto_now_add=True)
