from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.create_pluggy_connect_token_request_dto import CreatePluggyConnectTokenRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.pluggy_connect_token_entity import PluggyConnectTokenEntity
from python_core_api_sdk import util


async def pluggy_controller_create(request: web.Request, body) -> web.Response:
    """pluggy_controller_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreatePluggyConnectTokenRequestDto.from_dict(body)
    return web.Response(status=200)


async def pluggy_controller_webhook(request: web.Request, ) -> web.Response:
    """pluggy_controller_webhook

    


    """
    return web.Response(status=200)
