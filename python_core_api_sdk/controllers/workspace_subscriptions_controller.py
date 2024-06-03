from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.workspace_subscription_entity import WorkspaceSubscriptionEntity
from python_core_api_sdk import util


async def workspace_subscriptions_controller_get(request: web.Request, workspace_id) -> web.Response:
    """workspace_subscriptions_controller_get

    

    :param workspace_id: 
    :type workspace_id: str

    """
    return web.Response(status=200)
