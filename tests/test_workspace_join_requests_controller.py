# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.workspace_join_request_entity import WorkspaceJoinRequestEntity


pytestmark = pytest.mark.asyncio

async def test_workspace_join_requests_controller_create_new_pending_or_return_current(client):
    """Test case for workspace_join_requests_controller_create_new_pending_or_return_current

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/workspaces/{workspace_id}/join-requests'.format(workspace_id='workspace_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

