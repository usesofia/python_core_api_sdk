# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.subscription_product_entity import SubscriptionProductEntity


pytestmark = pytest.mark.asyncio

async def test_subscription_products_controller_list(client):
    """Test case for subscription_products_controller_list

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/subscription-products'.format(workspace_id='workspace_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

