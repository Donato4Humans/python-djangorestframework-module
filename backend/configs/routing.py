from django.urls import path

from channels.routing import URLRouter

from apps.chat.routing import websocket_urlpatterns as chat_routing
from apps.pizza.routing import websocket_urlpatterns as pizza_routing

# same as urls for http routing, but for websockets
websocket_urlpatterns = [
    path('api/chat/', URLRouter(chat_routing)),
    path('api/pizzas/', URLRouter(pizza_routing))
]