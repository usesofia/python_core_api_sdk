from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.bank_transaction_tag_entity import BankTransactionTagEntity
from python_core_api_sdk.models.create_bank_transaction_tag_request_dto import CreateBankTransactionTagRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk import util


async def bank_transaction_tags_controller_create_tag(request: web.Request, workspace_id, body) -> web.Response:
    """bank_transaction_tags_controller_create_tag

    

    :param workspace_id: 
    :type workspace_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateBankTransactionTagRequestDto.from_dict(body)
    return web.Response(status=200)


async def bank_transaction_tags_controller_list_tags(request: web.Request, workspace_id) -> web.Response:
    """bank_transaction_tags_controller_list_tags

    

    :param workspace_id: 
    :type workspace_id: str

    """
    return web.Response(status=200)
