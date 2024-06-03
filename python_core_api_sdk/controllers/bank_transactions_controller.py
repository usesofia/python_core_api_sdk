from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.bank_transaction_entity import BankTransactionEntity
from python_core_api_sdk.models.bank_transactions_page_entity import BankTransactionsPageEntity
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto import CreateOrUpdateBankTransactionsInBulkRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.update_bank_transaction_request_dto import UpdateBankTransactionRequestDto
from python_core_api_sdk import util


async def bank_transactions_controller_create_or_update_bank_transactions_in_bulk(request: web.Request, body) -> web.Response:
    """bank_transactions_controller_create_or_update_bank_transactions_in_bulk

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrUpdateBankTransactionsInBulkRequestDto.from_dict(body)
    return web.Response(status=200)


async def bank_transactions_controller_get_bank_transactions(request: web.Request, workspace_id, page_index=None, page_size=None, account_ids=None, category_ids=None, tag_ids=None, legal_natures=None, types=None, min_posted_date=None, max_posted_date=None, min_competency_date=None, max_competency_date=None, show_ignored=None, ignore_automatic_application_related=None, ignore_internal_transfers=None, ignore_invoice_related=None) -> web.Response:
    """bank_transactions_controller_get_bank_transactions

    

    :param workspace_id: 
    :type workspace_id: str
    :param page_index: 
    :type page_index: 
    :param page_size: 
    :type page_size: 
    :param account_ids: 
    :type account_ids: str
    :param category_ids: 
    :type category_ids: str
    :param tag_ids: 
    :type tag_ids: str
    :param legal_natures: 
    :type legal_natures: str
    :param types: 
    :type types: str
    :param min_posted_date: 
    :type min_posted_date: str
    :param max_posted_date: 
    :type max_posted_date: str
    :param min_competency_date: 
    :type min_competency_date: str
    :param max_competency_date: 
    :type max_competency_date: str
    :param show_ignored: 
    :type show_ignored: bool
    :param ignore_automatic_application_related: 
    :type ignore_automatic_application_related: bool
    :param ignore_internal_transfers: 
    :type ignore_internal_transfers: bool
    :param ignore_invoice_related: 
    :type ignore_invoice_related: bool

    """
    return web.Response(status=200)


async def bank_transactions_controller_get_bank_transactions_confirmed_today_by_me(request: web.Request, workspace_id, page_index=None, page_size=None) -> web.Response:
    """bank_transactions_controller_get_bank_transactions_confirmed_today_by_me

    

    :param workspace_id: 
    :type workspace_id: str
    :param page_index: 
    :type page_index: 
    :param page_size: 
    :type page_size: 

    """
    return web.Response(status=200)


async def bank_transactions_controller_get_bank_transactions_not_confirmed(request: web.Request, workspace_id, page_index=None, page_size=None, consider_ignored=None) -> web.Response:
    """bank_transactions_controller_get_bank_transactions_not_confirmed

    

    :param workspace_id: 
    :type workspace_id: str
    :param page_index: 
    :type page_index: 
    :param page_size: 
    :type page_size: 
    :param consider_ignored: 
    :type consider_ignored: bool

    """
    return web.Response(status=200)


async def bank_transactions_controller_get_bank_transactions_totals(request: web.Request, workspace_id, account_ids=None, category_ids=None, tag_ids=None, legal_natures=None, min_posted_date=None, max_posted_date=None, min_competency_date=None, max_competency_date=None, show_ignored=None, ignore_automatic_application_related=None, ignore_internal_transfers=None, ignore_invoice_related=None, types=None) -> web.Response:
    """bank_transactions_controller_get_bank_transactions_totals

    

    :param workspace_id: 
    :type workspace_id: str
    :param account_ids: 
    :type account_ids: str
    :param category_ids: 
    :type category_ids: str
    :param tag_ids: 
    :type tag_ids: str
    :param legal_natures: 
    :type legal_natures: str
    :param min_posted_date: 
    :type min_posted_date: str
    :param max_posted_date: 
    :type max_posted_date: str
    :param min_competency_date: 
    :type min_competency_date: str
    :param max_competency_date: 
    :type max_competency_date: str
    :param show_ignored: 
    :type show_ignored: bool
    :param ignore_automatic_application_related: 
    :type ignore_automatic_application_related: bool
    :param ignore_internal_transfers: 
    :type ignore_internal_transfers: bool
    :param ignore_invoice_related: 
    :type ignore_invoice_related: bool
    :param types: 
    :type types: str

    """
    return web.Response(status=200)


async def bank_transactions_controller_get_recent(request: web.Request, workspace_id) -> web.Response:
    """bank_transactions_controller_get_recent

    

    :param workspace_id: 
    :type workspace_id: str

    """
    return web.Response(status=200)


async def bank_transactions_controller_get_transaction_details(request: web.Request, bank_transaction_id) -> web.Response:
    """bank_transactions_controller_get_transaction_details

    

    :param bank_transaction_id: 
    :type bank_transaction_id: str

    """
    return web.Response(status=200)


async def bank_transactions_controller_update_transaction(request: web.Request, bank_transaction_id, body) -> web.Response:
    """bank_transactions_controller_update_transaction

    

    :param bank_transaction_id: 
    :type bank_transaction_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateBankTransactionRequestDto.from_dict(body)
    return web.Response(status=200)
