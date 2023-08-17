

from django.urls import path

import os
from game.consumers import GAMEBUILDER

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TicTacToe.settings')

websocket_urlpatterns = [
    path('ws/game/<room_code>',GAMEBUILDER.as_asgi())
]
# websocket_urlpatterns = [<URLPattern 'ws/game/<room_code>'>]



application = ProtocolTypeRouter(
    {
    'websocket':AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
    }
)
# application  = <channels.routing.ProtocolTypeRouter object at 0x000002231DB453D0>



