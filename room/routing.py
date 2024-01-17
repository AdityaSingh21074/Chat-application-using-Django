from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r'ws/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]