from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.checkout_session_entity import CheckoutSessionEntity
from python_core_api_sdk.models.create_stripe_checkout_session_request_dto import CreateStripeCheckoutSessionRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk import util


async def stripe_controller_create_checkout_session_for_stripe(request: web.Request, body) -> web.Response:
    """stripe_controller_create_checkout_session_for_stripe

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateStripeCheckoutSessionRequestDto.from_dict(body)
    return web.Response(status=200)


async def stripe_controller_stripe_webhook(request: web.Request, stripe_signature) -> web.Response:
    """stripe_controller_stripe_webhook

    

    :param stripe_signature: 
    :type stripe_signature: str

    """
    return web.Response(status=200)
