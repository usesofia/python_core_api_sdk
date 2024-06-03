from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.create_profile_request_dto import CreateProfileRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.parcial_update_profile_request_dto import ParcialUpdateProfileRequestDto
from python_core_api_sdk.models.profile_entity import ProfileEntity
from python_core_api_sdk import util


async def profiles_controller_create(request: web.Request, body) -> web.Response:
    """profiles_controller_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateProfileRequestDto.from_dict(body)
    return web.Response(status=200)


async def profiles_controller_get_my(request: web.Request, ) -> web.Response:
    """profiles_controller_get_my

    


    """
    return web.Response(status=200)


async def profiles_controller_parcial_update(request: web.Request, body) -> web.Response:
    """profiles_controller_parcial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = ParcialUpdateProfileRequestDto.from_dict(body)
    return web.Response(status=200)
