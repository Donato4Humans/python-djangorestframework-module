from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from core.services.jwt_service import JWTService, SocketToken


@database_sync_to_async
def get_user(token:str|None):
    try:
        return JWTService.verify_token(token, SocketToken)
    except (Exception,):
        pass

class AuthSocketMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send): # scope is same as request in http routing
        token = dict(
            [item.split('=') for item in scope['query_string'].decode('utf-8').split('&') if item]
        ).get('token', None)
        # in above line we iterate through query_string from scope, decode it from binary, split it by &(if more than 1 url-params),
        # split it by = for key/value and get token value(if no token, make it None)
        scope['user'] = await get_user(token=token)
        return await super().__call__(scope, receive, send)