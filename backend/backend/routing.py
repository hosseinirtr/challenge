from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/progress/', consumers.ProgressConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})