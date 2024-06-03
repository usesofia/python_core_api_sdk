# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.bank_transaction_category_entity import BankTransactionCategoryEntity
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity


pytestmark = pytest.mark.asyncio

async def test_bank_transaction_categories_controller_get_bank_transaction_categories(client):
    """Test case for bank_transaction_categories_controller_get_bank_transaction_categories

    
    """
    params = [('onlyLeafs', True),
                    ('transactionNatures', 'transaction_natures_example'),
                    ('legalNatures', 'legal_natures_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/bank/transactions/categories'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

