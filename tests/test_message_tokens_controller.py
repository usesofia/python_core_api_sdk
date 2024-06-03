# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.create_or_update_message_token_request_dto import CreateOrUpdateMessageTokenRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.message_token_entity import MessageTokenEntity


pytestmark = pytest.mark.asyncio

async def test_message_tokens_controller_create_or_update_message_token(client):
    """Test case for message_tokens_controller_create_or_update_message_token

    
    """
    body = {"deviceId":"deviceId","platform":"platform","token":"token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/workspaces/{workspace_id}/message-tokens'.format(workspace_id='workspace_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_message_tokens_controller_get_workspace_message_tokens(client):
    """Test case for message_tokens_controller_get_workspace_message_tokens

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/message-tokens'.format(workspace_id='workspace_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

