from django.urls import path

from channels.routing import URLRouter

from apps.chat.routing import websocket_urlpatterns as chat_routing

# same as urls for http routing, but for websockets
websocket_urlpatterns = [
    path('api/chat/', URLRouter(chat_routing))
]