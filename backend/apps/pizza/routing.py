from django.urls import path

from apps.pizza.consumers import PizzaConsumer

websocket_urlpatterns = [
    path('', PizzaConsumer.as_asgi())
]