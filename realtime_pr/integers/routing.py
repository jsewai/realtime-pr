from django.urls import path
# ws as websocket
from .consumers import WSConsumer


ws_urlpatterns = [
  path('ws/some_url/', WSConsumer.as_asgi())
]