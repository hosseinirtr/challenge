from django.urls import path
from .views import RegisterView, ObtainTokenView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('api_token_auth/', ObtainTokenView.as_view(), name='api_token_auth'),
]

