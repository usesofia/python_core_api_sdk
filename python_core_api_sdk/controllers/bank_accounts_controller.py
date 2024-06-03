from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.bank_account_entity import BankAccountEntity
from python_core_api_sdk.models.bank_accounts_balance_report_entity import BankAccountsBalanceReportEntity
from python_core_api_sdk.models.create_or_update_bank_account_request_dto import CreateOrUpdateBankAccountRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk import util


async def bank_accounts_controller_activate_bank_account(request: web.Request, bank_account_id) -> web.Response:
    """bank_accounts_controller_activate_bank_account

    

    :param bank_account_id: 
    :type bank_account_id: str

    """
    return web.Response(status=200)


async def bank_accounts_controller_create_or_update_bank_account(request: web.Request, workspace_id, body) -> web.Response:
    """bank_accounts_controller_create_or_update_bank_account

    

    :param workspace_id: 
    :type workspace_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrUpdateBankAccountRequestDto.from_dict(body)
    return web.Response(status=200)


async def bank_accounts_controller_create_workspace_bank_accounts_balance_report(request: web.Request, workspace_id, enabled=None, types=None) -> web.Response:
    """bank_accounts_controller_create_workspace_bank_accounts_balance_report

    

    :param workspace_id: 
    :type workspace_id: str
    :param enabled: 
    :type enabled: bool
    :param types: 
    :type types: str

    """
    return web.Response(status=200)


async def bank_accounts_controller_disable_bank_account(request: web.Request, bank_account_id) -> web.Response:
    """bank_accounts_controller_disable_bank_account

    

    :param bank_account_id: 
    :type bank_account_id: str

    """
    return web.Response(status=200)


async def bank_accounts_controller_fetch_connection_bank_accounts(request: web.Request, workspace_id, bank_connection_id, enabled, types) -> web.Response:
    """bank_accounts_controller_fetch_connection_bank_accounts

    

    :param workspace_id: 
    :type workspace_id: str
    :param bank_connection_id: 
    :type bank_connection_id: str
    :param enabled: 
    :type enabled: bool
    :param types: 
    :type types: str

    """
    return web.Response(status=200)


async def bank_accounts_controller_fetch_workspace_bank_accounts(request: web.Request, workspace_id, enabled=None, types=None) -> web.Response:
    """bank_accounts_controller_fetch_workspace_bank_accounts

    

    :param workspace_id: 
    :type workspace_id: str
    :param enabled: 
    :type enabled: bool
    :param types: 
    :type types: str

    """
    return web.Response(status=200)


async def bank_accounts_controller_get_bank_account_details(request: web.Request, bank_account_id) -> web.Response:
    """bank_accounts_controller_get_bank_account_details

    

    :param bank_account_id: 
    :type bank_account_id: str

    """
    return web.Response(status=200)
