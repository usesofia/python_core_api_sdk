# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.create_pluggy_connect_token_request_dto import CreatePluggyConnectTokenRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.pluggy_connect_token_entity import PluggyConnectTokenEntity


pytestmark = pytest.mark.asyncio

async def test_pluggy_controller_create(client):
    """Test case for pluggy_controller_create

    
    """
    body = {"itemId":"itemId","historyRange":"historyRange","workspaceId":"workspaceId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/pluggy/connect-token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pluggy_controller_webhook(client):
    """Test case for pluggy_controller_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/pluggy/webhook',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

