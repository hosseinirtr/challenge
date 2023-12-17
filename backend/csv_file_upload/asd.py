from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CSVUpload

class CSVUploadViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('csv_upload')
        self.csv_content = b'column1,column2\nvalue1,value2\n'
        self.csv_file = SimpleUploadedFile('test.csv', self.csv_content)

    def test_csv_upload(self):
        response = self.client.post(self.url, {'file': self.csv_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CSVUpload.objects.count(), 1)
        csv_upload = CSVUpload.objects.first()
        self.assertEqual(csv_upload.file.read(), self.csv_content)