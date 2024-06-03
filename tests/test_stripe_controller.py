# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.checkout_session_entity import CheckoutSessionEntity
from python_core_api_sdk.models.create_stripe_checkout_session_request_dto import CreateStripeCheckoutSessionRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity


pytestmark = pytest.mark.asyncio

async def test_stripe_controller_create_checkout_session_for_stripe(client):
    """Test case for stripe_controller_create_checkout_session_for_stripe

    
    """
    body = {"priceId":"priceId","isTrial":True,"workspaceId":"workspaceId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/stripe/checkout-session',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stripe_controller_stripe_webhook(client):
    """Test case for stripe_controller_stripe_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'stripe_signature': 'stripe_signature_example',
    }
    response = await client.request(
        method='POST',
        path='/stripe/webhook',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

