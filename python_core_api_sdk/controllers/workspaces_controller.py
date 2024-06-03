from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.create_workspace_request_dto import CreateWorkspaceRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.parcial_update_workspace_request_dto import ParcialUpdateWorkspaceRequestDto
from python_core_api_sdk.models.user_related_workspace_entity import UserRelatedWorkspaceEntity
from python_core_api_sdk.models.workspace_entity import WorkspaceEntity
from python_core_api_sdk import util


async def workspaces_controller_create(request: web.Request, body) -> web.Response:
    """workspaces_controller_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateWorkspaceRequestDto.from_dict(body)
    return web.Response(status=200)


async def workspaces_controller_fetch_user_related_workspaces(request: web.Request, ) -> web.Response:
    """workspaces_controller_fetch_user_related_workspaces

    


    """
    return web.Response(status=200)


async def workspaces_controller_get(request: web.Request, workspace_id) -> web.Response:
    """workspaces_controller_get

    

    :param workspace_id: 
    :type workspace_id: str

    """
    return web.Response(status=200)


async def workspaces_controller_parcial_update(request: web.Request, workspace_id, body) -> web.Response:
    """workspaces_controller_parcial_update

    

    :param workspace_id: 
    :type workspace_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ParcialUpdateWorkspaceRequestDto.from_dict(body)
    return web.Response(status=200)
