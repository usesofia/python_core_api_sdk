# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_auth_controller_check_email_in_use(client):
    """Test case for auth_controller_check_email_in_use

    
    """
    body = {"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/check-email-in-use',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_controller_refresh(client):
    """Test case for auth_controller_refresh

    
    """
    body = {"clientId":"clientId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/refresh',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_controller_send_email_verification_code(client):
    """Test case for auth_controller_send_email_verification_code

    
    """
    body = {"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/sign-up/email-verification-code',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_controller_sign_in_with_email_password(client):
    """Test case for auth_controller_sign_in_with_email_password

    
    """
    body = {"password":"password","clientId":"clientId","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/sign-in/email-password',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_controller_sign_up_with_email_password(client):
    """Test case for auth_controller_sign_up_with_email_password

    
    """
    body = {"password":"password","email":"email","emailVerificationCode":"emailVerificationCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/sign-up/email-password',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

