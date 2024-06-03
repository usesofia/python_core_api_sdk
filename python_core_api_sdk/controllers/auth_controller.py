from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.check_email_in_use_request_dto import CheckEmailInUseRequestDto
from python_core_api_sdk.models.credentials_entity import CredentialsEntity
from python_core_api_sdk.models.email_in_use_entity import EmailInUseEntity
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.refresh_request_dto import RefreshRequestDto
from python_core_api_sdk.models.send_email_verification_code_request_dto import SendEmailVerificationCodeRequestDto
from python_core_api_sdk.models.sign_in_with_email_password_request_dto import SignInWithEmailPasswordRequestDto
from python_core_api_sdk.models.sign_up_with_email_password_request_dto import SignUpWithEmailPasswordRequestDto
from python_core_api_sdk.models.user_entity import UserEntity
from python_core_api_sdk import util


async def auth_controller_check_email_in_use(request: web.Request, body) -> web.Response:
    """auth_controller_check_email_in_use

    

    :param body: 
    :type body: dict | bytes

    """
    body = CheckEmailInUseRequestDto.from_dict(body)
    return web.Response(status=200)


async def auth_controller_refresh(request: web.Request, body) -> web.Response:
    """auth_controller_refresh

    

    :param body: 
    :type body: dict | bytes

    """
    body = RefreshRequestDto.from_dict(body)
    return web.Response(status=200)


async def auth_controller_send_email_verification_code(request: web.Request, body) -> web.Response:
    """auth_controller_send_email_verification_code

    

    :param body: 
    :type body: dict | bytes

    """
    body = SendEmailVerificationCodeRequestDto.from_dict(body)
    return web.Response(status=200)


async def auth_controller_sign_in_with_email_password(request: web.Request, body) -> web.Response:
    """auth_controller_sign_in_with_email_password

    

    :param body: 
    :type body: dict | bytes

    """
    body = SignInWithEmailPasswordRequestDto.from_dict(body)
    return web.Response(status=200)


async def auth_controller_sign_up_with_email_password(request: web.Request, body) -> web.Response:
    """auth_controller_sign_up_with_email_password

    

    :param body: 
    :type body: dict | bytes

    """
    body = SignUpWithEmailPasswordRequestDto.from_dict(body)
    return web.Response(status=200)
