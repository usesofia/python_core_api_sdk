# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.bank_account_entity import BankAccountEntity
from python_core_api_sdk.models.bank_accounts_balance_report_entity import BankAccountsBalanceReportEntity
from python_core_api_sdk.models.create_or_update_bank_account_request_dto import CreateOrUpdateBankAccountRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_controller_activate_bank_account(client):
    """Test case for bank_accounts_controller_activate_bank_account

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bank/accounts/{bank_account_id}/activate'.format(bank_account_id='bank_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_controller_create_or_update_bank_account(client):
    """Test case for bank_accounts_controller_create_or_update_bank_account

    
    """
    body = {"number":"number","bankConnectionId":"bankConnectionId","balance":0.8008281904610115,"provider":"provider","providerAccountId":"providerAccountId","name":"name","type":"type","currencyCode":"currencyCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/workspaces/{workspace_id}/bank/accounts'.format(workspace_id='workspace_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_controller_create_workspace_bank_accounts_balance_report(client):
    """Test case for bank_accounts_controller_create_workspace_bank_accounts_balance_report

    
    """
    params = [('enabled', True),
                    ('types', 'types_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/workspaces/{workspace_id}/bank/accounts/balance-report'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_controller_disable_bank_account(client):
    """Test case for bank_accounts_controller_disable_bank_account

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/bank/accounts/{bank_account_id}/disable'.format(bank_account_id='bank_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_controller_fetch_connection_bank_accounts(client):
    """Test case for bank_accounts_controller_fetch_connection_bank_accounts

    
    """
    params = [('enabled', True),
                    ('types', 'types_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/bank/connections/{bank_connection_id}/accounts'.format(workspace_id='workspace_id_example', bank_connection_id='bank_connection_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_controller_fetch_workspace_bank_accounts(client):
    """Test case for bank_accounts_controller_fetch_workspace_bank_accounts

    
    """
    params = [('enabled', True),
                    ('types', 'types_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/bank/accounts'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_controller_get_bank_account_details(client):
    """Test case for bank_accounts_controller_get_bank_account_details

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/bank/accounts/{bank_account_id}'.format(bank_account_id='bank_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

