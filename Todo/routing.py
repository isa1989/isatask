from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from app import consumers



application = ProtocolTypeRouter({
         "websocket": AllowedHostsOriginValidator(
             AuthMiddlewareStack(
                 URLRouter([
                     url(r'^app/detail/(?P<pk>[0-9]+)$', consumers.CommentConsumer),
                 ])

         )

    )
})



