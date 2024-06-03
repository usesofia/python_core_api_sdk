from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.workspace_join_request_entity import WorkspaceJoinRequestEntity
from python_core_api_sdk import util


async def workspace_join_requests_controller_create_new_pending_or_return_current(request: web.Request, workspace_id) -> web.Response:
    """workspace_join_requests_controller_create_new_pending_or_return_current

    

    :param workspace_id: 
    :type workspace_id: str

    """
    return web.Response(status=200)
