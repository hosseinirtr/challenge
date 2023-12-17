from django.urls import path
from .views import CSVUploadView,ViewAllCustomer

urlpatterns = [
    path('upload/', CSVUploadView.as_view(), name='csv_upload'),
    path('all/', ViewAllCustomer.as_view(), name='csv_upload'),
]