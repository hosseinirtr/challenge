from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile

from csv_file_upload.models import CSVUpload, Customer
from .views import CSVUploadView

class CSVUploadViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        print("User -> ", self.user)
    
    def test_csv_upload(self):
        # Create a mock CSV file
        csv_file = SimpleUploadedFile("test.csv", b"1,test1@example.com\n2,test2@example.com\n3,test3@example.com", content_type="text/csv")
        
        # Create a request with the CSV file
        request = self.factory.post('/upload/', {'file': csv_file}, format='multipart')
        request.user = self.user
        request.META['authorization'] = 'Token your-token-here'  # Add authentication token
        
        # Call the view
        view = CSVUploadView.as_view()
        response = view(request)
        
        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        
        # Assert that the CSVUpload and Customer objects are created
        self.assertEqual(CSVUpload.objects.count(), 1)
        self.assertEqual(Customer.objects.count(), 3)