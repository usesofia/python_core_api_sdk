from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.bank_transaction_category_entity import BankTransactionCategoryEntity
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk import util


async def bank_transaction_categories_controller_get_bank_transaction_categories(request: web.Request, workspace_id, only_leafs=None, transaction_natures=None, legal_natures=None) -> web.Response:
    """bank_transaction_categories_controller_get_bank_transaction_categories

    

    :param workspace_id: 
    :type workspace_id: str
    :param only_leafs: 
    :type only_leafs: bool
    :param transaction_natures: 
    :type transaction_natures: str
    :param legal_natures: 
    :type legal_natures: str

    """
    return web.Response(status=200)
