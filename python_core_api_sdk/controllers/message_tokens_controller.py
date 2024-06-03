from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.create_or_update_message_token_request_dto import CreateOrUpdateMessageTokenRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.message_token_entity import MessageTokenEntity
from python_core_api_sdk import util


async def message_tokens_controller_create_or_update_message_token(request: web.Request, workspace_id, body) -> web.Response:
    """message_tokens_controller_create_or_update_message_token

    

    :param workspace_id: 
    :type workspace_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrUpdateMessageTokenRequestDto.from_dict(body)
    return web.Response(status=200)


async def message_tokens_controller_get_workspace_message_tokens(request: web.Request, workspace_id) -> web.Response:
    """message_tokens_controller_get_workspace_message_tokens

    

    :param workspace_id: 
    :type workspace_id: str

    """
    return web.Response(status=200)
