# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.create_profile_request_dto import CreateProfileRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.parcial_update_profile_request_dto import ParcialUpdateProfileRequestDto
from python_core_api_sdk.models.profile_entity import ProfileEntity


pytestmark = pytest.mark.asyncio

async def test_profiles_controller_create(client):
    """Test case for profiles_controller_create

    
    """
    body = {"phone":"phone","fullName":"fullName","birthDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/profiles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_controller_get_my(client):
    """Test case for profiles_controller_get_my

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/profiles/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_controller_parcial_update(client):
    """Test case for profiles_controller_parcial_update

    
    """
    body = {"phone":"phone","fullName":"fullName","birthDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/profiles/me',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

