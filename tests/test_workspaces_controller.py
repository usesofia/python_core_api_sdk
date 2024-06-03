# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.create_workspace_request_dto import CreateWorkspaceRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.parcial_update_workspace_request_dto import ParcialUpdateWorkspaceRequestDto
from python_core_api_sdk.models.user_related_workspace_entity import UserRelatedWorkspaceEntity
from python_core_api_sdk.models.workspace_entity import WorkspaceEntity


pytestmark = pytest.mark.asyncio

async def test_workspaces_controller_create(client):
    """Test case for workspaces_controller_create

    
    """
    body = {"businessSegment":"businessSegment","name":"name","type":"type","prettyId":"prettyId","otherDescription":"otherDescription"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/workspaces',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_controller_fetch_user_related_workspaces(client):
    """Test case for workspaces_controller_fetch_user_related_workspaces

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/related-to-me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_controller_get(client):
    """Test case for workspaces_controller_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}'.format(workspace_id='workspace_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_controller_parcial_update(client):
    """Test case for workspaces_controller_parcial_update

    
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/workspaces/{workspace_id}'.format(workspace_id='workspace_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

