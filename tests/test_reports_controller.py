# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.bank_transaction_indicator_entity import BankTransactionIndicatorEntity
from python_core_api_sdk.models.cash_flow_by_category_report_entity import CashFlowByCategoryReportEntity
from python_core_api_sdk.models.cash_flow_report_entity import CashFlowReportEntity
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.financial_statement_report import FinancialStatementReport


pytestmark = pytest.mark.asyncio

async def test_reports_controller_get_accounts_entries_by_category_report(client):
    """Test case for reports_controller_get_accounts_entries_by_category_report

    
    """
    params = [('accountIds', 'account_ids_example'),
                    ('tagIds', 'tag_ids_example'),
                    ('legalNatures', 'legal_natures_example'),
                    ('considerIgnored', True),
                    ('ignoreInternalTransfers', True),
                    ('ignoreAutomaticApplicationRelated', True),
                    ('minPostedDate', 'min_posted_date_example'),
                    ('maxPostedDate', 'max_posted_date_example'),
                    ('minCompetencyDate', 'min_competency_date_example'),
                    ('maxCompetencyDate', 'max_competency_date_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/reports/accounts/entries-by-category'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_controller_get_accounts_outputs_by_category_report(client):
    """Test case for reports_controller_get_accounts_outputs_by_category_report

    
    """
    params = [('accountIds', 'account_ids_example'),
                    ('tagIds', 'tag_ids_example'),
                    ('legalNatures', 'legal_natures_example'),
                    ('considerIgnored', True),
                    ('ignoreInternalTransfers', True),
                    ('ignoreAutomaticApplicationRelated', True),
                    ('minPostedDate', 'min_posted_date_example'),
                    ('maxPostedDate', 'max_posted_date_example'),
                    ('minCompetencyDate', 'min_competency_date_example'),
                    ('maxCompetencyDate', 'max_competency_date_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/reports/accounts/outputs-by-category'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_controller_get_business_indicators(client):
    """Test case for reports_controller_get_business_indicators

    
    """
    params = [('accountIds', 'account_ids_example'),
                    ('tagIds', 'tag_ids_example'),
                    ('considerIgnored', True),
                    ('minPostedDate', 'min_posted_date_example'),
                    ('maxPostedDate', 'max_posted_date_example'),
                    ('minCompetencyDate', 'min_competency_date_example'),
                    ('maxCompetencyDate', 'max_competency_date_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/reports/indicators/business'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_controller_get_cards_cash_flow_report(client):
    """Test case for reports_controller_get_cards_cash_flow_report

    
    """
    params = [('accountIds', 'account_ids_example'),
                    ('categoryIds', 'category_ids_example'),
                    ('tagIds', 'tag_ids_example'),
                    ('legalNatures', 'legal_natures_example'),
                    ('considerIgnored', True),
                    ('ignoreInvoiceRelated', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/reports/cards/cash-flow'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_controller_get_cards_outputs_by_category_report(client):
    """Test case for reports_controller_get_cards_outputs_by_category_report

    
    """
    params = [('accountIds', 'account_ids_example'),
                    ('tagIds', 'tag_ids_example'),
                    ('legalNatures', 'legal_natures_example'),
                    ('considerIgnored', True),
                    ('minPostedDate', 'min_posted_date_example'),
                    ('maxPostedDate', 'max_posted_date_example'),
                    ('minCompetencyDate', 'min_competency_date_example'),
                    ('maxCompetencyDate', 'max_competency_date_example'),
                    ('ignoreInvoiceRelated', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/reports/cards/outputs-by-category'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_controller_get_cash_flow_report(client):
    """Test case for reports_controller_get_cash_flow_report

    
    """
    params = [('accountIds', 'account_ids_example'),
                    ('categoryIds', 'category_ids_example'),
                    ('tagIds', 'tag_ids_example'),
                    ('legalNatures', 'legal_natures_example'),
                    ('considerIgnored', True),
                    ('ignoreInternalTransfers', True),
                    ('ignoreAutomaticApplicationRelated', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/reports/accounts/cash-flow'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_controller_get_financial_statement_report(client):
    """Test case for reports_controller_get_financial_statement_report

    
    """
    params = [('accountIds', 'account_ids_example'),
                    ('tagIds', 'tag_ids_example'),
                    ('legalNatures', 'legal_natures_example'),
                    ('considerIgnored', True),
                    ('minPostedDate', 'min_posted_date_example'),
                    ('maxPostedDate', 'max_posted_date_example'),
                    ('minCompetencyDate', 'min_competency_date_example'),
                    ('maxCompetencyDate', 'max_competency_date_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/reports/financial-statement'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

