# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.bank_connection_entity import BankConnectionEntity
from python_core_api_sdk.models.bank_connection_with_accounts_entity import BankConnectionWithAccountsEntity
from python_core_api_sdk.models.create_or_update_bank_connection_request_dto import CreateOrUpdateBankConnectionRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity


pytestmark = pytest.mark.asyncio

async def test_bank_connections_controller_activate_bank_connection(client):
    """Test case for bank_connections_controller_activate_bank_connection

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bank/connections/{bank_connection_id}/activate'.format(bank_connection_id='bank_connection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_connections_controller_create_or_update_bank_connection(client):
    """Test case for bank_connections_controller_create_or_update_bank_connection

    
    """
    body = {"createdByUserId":"createdByUserId","providerItemId":"providerItemId","historyRange":"historyRange","provider":"provider","providerConnectorId":"providerConnectorId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/workspaces/{workspace_id}/bank/connections'.format(workspace_id='workspace_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_connections_controller_disable_bank_connection(client):
    """Test case for bank_connections_controller_disable_bank_connection

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bank/connections/{bank_connection_id}/disable'.format(bank_connection_id='bank_connection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_connections_controller_fetch_user_bank_connections(client):
    """Test case for bank_connections_controller_fetch_user_bank_connections

    
    """
    params = [('enabled', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/bank/connections'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_connections_controller_get_bank_connection_details(client):
    """Test case for bank_connections_controller_get_bank_connection_details

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/bank/connections/{bank_connection_id}'.format(bank_connection_id='bank_connection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

