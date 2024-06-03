from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.subscription_product_entity import SubscriptionProductEntity
from python_core_api_sdk import util


async def subscription_products_controller_list(request: web.Request, workspace_id) -> web.Response:
    """subscription_products_controller_list

    

    :param workspace_id: 
    :type workspace_id: str

    """
    return web.Response(status=200)
