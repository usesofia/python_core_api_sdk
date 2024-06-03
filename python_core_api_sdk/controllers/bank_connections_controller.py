from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.bank_connection_entity import BankConnectionEntity
from python_core_api_sdk.models.bank_connection_with_accounts_entity import BankConnectionWithAccountsEntity
from python_core_api_sdk.models.create_or_update_bank_connection_request_dto import CreateOrUpdateBankConnectionRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk import util


async def bank_connections_controller_activate_bank_connection(request: web.Request, bank_connection_id) -> web.Response:
    """bank_connections_controller_activate_bank_connection

    

    :param bank_connection_id: 
    :type bank_connection_id: str

    """
    return web.Response(status=200)


async def bank_connections_controller_create_or_update_bank_connection(request: web.Request, workspace_id, body) -> web.Response:
    """bank_connections_controller_create_or_update_bank_connection

    

    :param workspace_id: 
    :type workspace_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrUpdateBankConnectionRequestDto.from_dict(body)
    return web.Response(status=200)


async def bank_connections_controller_disable_bank_connection(request: web.Request, bank_connection_id) -> web.Response:
    """bank_connections_controller_disable_bank_connection

    

    :param bank_connection_id: 
    :type bank_connection_id: str

    """
    return web.Response(status=200)


async def bank_connections_controller_fetch_user_bank_connections(request: web.Request, workspace_id, enabled=None) -> web.Response:
    """bank_connections_controller_fetch_user_bank_connections

    

    :param workspace_id: 
    :type workspace_id: str
    :param enabled: 
    :type enabled: bool

    """
    return web.Response(status=200)


async def bank_connections_controller_get_bank_connection_details(request: web.Request, bank_connection_id) -> web.Response:
    """bank_connections_controller_get_bank_connection_details

    

    :param bank_connection_id: 
    :type bank_connection_id: str

    """
    return web.Response(status=200)
