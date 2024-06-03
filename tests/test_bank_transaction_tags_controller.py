# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.bank_transaction_tag_entity import BankTransactionTagEntity
from python_core_api_sdk.models.create_bank_transaction_tag_request_dto import CreateBankTransactionTagRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity


pytestmark = pytest.mark.asyncio

async def test_bank_transaction_tags_controller_create_tag(client):
    """Test case for bank_transaction_tags_controller_create_tag

    
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/workspaces/{workspace_id}/bank/transactions/tags'.format(workspace_id='workspace_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_transaction_tags_controller_list_tags(client):
    """Test case for bank_transaction_tags_controller_list_tags

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/bank/transactions/tags'.format(workspace_id='workspace_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

