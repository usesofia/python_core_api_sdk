# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.workspace_subscription_entity import WorkspaceSubscriptionEntity


pytestmark = pytest.mark.asyncio

async def test_workspace_subscriptions_controller_get(client):
    """Test case for workspace_subscriptions_controller_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/subscription'.format(workspace_id='workspace_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

