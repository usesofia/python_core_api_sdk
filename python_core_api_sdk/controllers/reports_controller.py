from typing import List, Dict
from aiohttp import web

from python_core_api_sdk.models.bank_transaction_indicator_entity import BankTransactionIndicatorEntity
from python_core_api_sdk.models.cash_flow_by_category_report_entity import CashFlowByCategoryReportEntity
from python_core_api_sdk.models.cash_flow_report_entity import CashFlowReportEntity
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.financial_statement_report import FinancialStatementReport
from python_core_api_sdk import util


async def reports_controller_get_accounts_entries_by_category_report(request: web.Request, workspace_id, account_ids=None, tag_ids=None, legal_natures=None, consider_ignored=None, ignore_internal_transfers=None, ignore_automatic_application_related=None, min_posted_date=None, max_posted_date=None, min_competency_date=None, max_competency_date=None) -> web.Response:
    """reports_controller_get_accounts_entries_by_category_report

    

    :param workspace_id: 
    :type workspace_id: str
    :param account_ids: 
    :type account_ids: str
    :param tag_ids: 
    :type tag_ids: str
    :param legal_natures: 
    :type legal_natures: str
    :param consider_ignored: 
    :type consider_ignored: bool
    :param ignore_internal_transfers: 
    :type ignore_internal_transfers: bool
    :param ignore_automatic_application_related: 
    :type ignore_automatic_application_related: bool
    :param min_posted_date: 
    :type min_posted_date: str
    :param max_posted_date: 
    :type max_posted_date: str
    :param min_competency_date: 
    :type min_competency_date: str
    :param max_competency_date: 
    :type max_competency_date: str

    """
    return web.Response(status=200)


async def reports_controller_get_accounts_outputs_by_category_report(request: web.Request, workspace_id, account_ids=None, tag_ids=None, legal_natures=None, consider_ignored=None, ignore_internal_transfers=None, ignore_automatic_application_related=None, min_posted_date=None, max_posted_date=None, min_competency_date=None, max_competency_date=None) -> web.Response:
    """reports_controller_get_accounts_outputs_by_category_report

    

    :param workspace_id: 
    :type workspace_id: str
    :param account_ids: 
    :type account_ids: str
    :param tag_ids: 
    :type tag_ids: str
    :param legal_natures: 
    :type legal_natures: str
    :param consider_ignored: 
    :type consider_ignored: bool
    :param ignore_internal_transfers: 
    :type ignore_internal_transfers: bool
    :param ignore_automatic_application_related: 
    :type ignore_automatic_application_related: bool
    :param min_posted_date: 
    :type min_posted_date: str
    :param max_posted_date: 
    :type max_posted_date: str
    :param min_competency_date: 
    :type min_competency_date: str
    :param max_competency_date: 
    :type max_competency_date: str

    """
    return web.Response(status=200)


async def reports_controller_get_business_indicators(request: web.Request, workspace_id, account_ids=None, tag_ids=None, consider_ignored=None, min_posted_date=None, max_posted_date=None, min_competency_date=None, max_competency_date=None) -> web.Response:
    """reports_controller_get_business_indicators

    

    :param workspace_id: 
    :type workspace_id: str
    :param account_ids: 
    :type account_ids: str
    :param tag_ids: 
    :type tag_ids: str
    :param consider_ignored: 
    :type consider_ignored: bool
    :param min_posted_date: 
    :type min_posted_date: str
    :param max_posted_date: 
    :type max_posted_date: str
    :param min_competency_date: 
    :type min_competency_date: str
    :param max_competency_date: 
    :type max_competency_date: str

    """
    return web.Response(status=200)


async def reports_controller_get_cards_cash_flow_report(request: web.Request, workspace_id, account_ids=None, category_ids=None, tag_ids=None, legal_natures=None, consider_ignored=None, ignore_invoice_related=None) -> web.Response:
    """reports_controller_get_cards_cash_flow_report

    

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
    :param consider_ignored: 
    :type consider_ignored: bool
    :param ignore_invoice_related: 
    :type ignore_invoice_related: bool

    """
    return web.Response(status=200)


async def reports_controller_get_cards_outputs_by_category_report(request: web.Request, workspace_id, account_ids=None, tag_ids=None, legal_natures=None, consider_ignored=None, min_posted_date=None, max_posted_date=None, min_competency_date=None, max_competency_date=None, ignore_invoice_related=None) -> web.Response:
    """reports_controller_get_cards_outputs_by_category_report

    

    :param workspace_id: 
    :type workspace_id: str
    :param account_ids: 
    :type account_ids: str
    :param tag_ids: 
    :type tag_ids: str
    :param legal_natures: 
    :type legal_natures: str
    :param consider_ignored: 
    :type consider_ignored: bool
    :param min_posted_date: 
    :type min_posted_date: str
    :param max_posted_date: 
    :type max_posted_date: str
    :param min_competency_date: 
    :type min_competency_date: str
    :param max_competency_date: 
    :type max_competency_date: str
    :param ignore_invoice_related: 
    :type ignore_invoice_related: bool

    """
    return web.Response(status=200)


async def reports_controller_get_cash_flow_report(request: web.Request, workspace_id, account_ids=None, category_ids=None, tag_ids=None, legal_natures=None, consider_ignored=None, ignore_internal_transfers=None, ignore_automatic_application_related=None) -> web.Response:
    """reports_controller_get_cash_flow_report

    

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
    :param consider_ignored: 
    :type consider_ignored: bool
    :param ignore_internal_transfers: 
    :type ignore_internal_transfers: bool
    :param ignore_automatic_application_related: 
    :type ignore_automatic_application_related: bool

    """
    return web.Response(status=200)


async def reports_controller_get_financial_statement_report(request: web.Request, workspace_id, account_ids=None, tag_ids=None, legal_natures=None, consider_ignored=None, min_posted_date=None, max_posted_date=None, min_competency_date=None, max_competency_date=None) -> web.Response:
    """reports_controller_get_financial_statement_report

    

    :param workspace_id: 
    :type workspace_id: str
    :param account_ids: 
    :type account_ids: str
    :param tag_ids: 
    :type tag_ids: str
    :param legal_natures: 
    :type legal_natures: str
    :param consider_ignored: 
    :type consider_ignored: bool
    :param min_posted_date: 
    :type min_posted_date: str
    :param max_posted_date: 
    :type max_posted_date: str
    :param min_competency_date: 
    :type min_competency_date: str
    :param max_competency_date: 
    :type max_competency_date: str

    """
    return web.Response(status=200)
