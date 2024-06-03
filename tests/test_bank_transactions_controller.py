# coding: utf-8

import pytest
import json
from aiohttp import web

from python_core_api_sdk.models.bank_transaction_entity import BankTransactionEntity
from python_core_api_sdk.models.bank_transactions_page_entity import BankTransactionsPageEntity
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto import CreateOrUpdateBankTransactionsInBulkRequestDto
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.update_bank_transaction_request_dto import UpdateBankTransactionRequestDto


pytestmark = pytest.mark.asyncio

async def test_bank_transactions_controller_create_or_update_bank_transactions_in_bulk(client):
    """Test case for bank_transactions_controller_create_or_update_bank_transactions_in_bulk

    
    """
    body = {"items":[{"amount":0.8008281904610115,"categoryGuesses":[{"score":2.3021358869347655,"origin":"origin","name":"name","categoryId":"categoryId"},{"score":2.3021358869347655,"origin":"origin","name":"name","categoryId":"categoryId"}],"providerTransactionId":"providerTransactionId","description":"description","type":"type","providerCategoryId":"providerCategoryId","postedDate":"2000-01-23T04:56:07.000+00:00","accountId":"accountId","competencyDate":"2000-01-23T04:56:07.000+00:00","provider":"provider","providerCategoryName":"providerCategoryName","bestGuessCategoryId":"bestGuessCategoryId","legalNature":"legalNature","paymentData":{"payerRoutingNumberISPB":"payerRoutingNumberISPB","reason":"reason","receiverDocumentNumberValue":"receiverDocumentNumberValue","receiverRoutingNumber":"receiverRoutingNumber","receiverName":"receiverName","payerRoutingNumber":"payerRoutingNumber","payerDocumentNumberType":"payerDocumentNumberType","payerAccountNumber":"payerAccountNumber","receiverReferenceId":"receiverReferenceId","payerDocumentNumberValue":"payerDocumentNumberValue","referenceNumber":"referenceNumber","receiverAccountNumber":"receiverAccountNumber","receiverDocumentNumberType":"receiverDocumentNumberType","payerName":"payerName","receiverBranchNumber":"receiverBranchNumber","paymentMethod":"paymentMethod","receiverRoutingNumberISPB":"receiverRoutingNumberISPB","payerBranchNumber":"payerBranchNumber"},"creditCardMetadata":{"installmentNumber":6.027456183070403,"totalInstallments":1.4658129805029452,"totalAmount":5.962133916683182,"billId":"billId","payeeMCC":5.637376656633329,"cardNumber":"cardNumber"},"categoryId":"categoryId","workspaceId":"workspaceId","status":"status"},{"amount":0.8008281904610115,"categoryGuesses":[{"score":2.3021358869347655,"origin":"origin","name":"name","categoryId":"categoryId"},{"score":2.3021358869347655,"origin":"origin","name":"name","categoryId":"categoryId"}],"providerTransactionId":"providerTransactionId","description":"description","type":"type","providerCategoryId":"providerCategoryId","postedDate":"2000-01-23T04:56:07.000+00:00","accountId":"accountId","competencyDate":"2000-01-23T04:56:07.000+00:00","provider":"provider","providerCategoryName":"providerCategoryName","bestGuessCategoryId":"bestGuessCategoryId","legalNature":"legalNature","paymentData":{"payerRoutingNumberISPB":"payerRoutingNumberISPB","reason":"reason","receiverDocumentNumberValue":"receiverDocumentNumberValue","receiverRoutingNumber":"receiverRoutingNumber","receiverName":"receiverName","payerRoutingNumber":"payerRoutingNumber","payerDocumentNumberType":"payerDocumentNumberType","payerAccountNumber":"payerAccountNumber","receiverReferenceId":"receiverReferenceId","payerDocumentNumberValue":"payerDocumentNumberValue","referenceNumber":"referenceNumber","receiverAccountNumber":"receiverAccountNumber","receiverDocumentNumberType":"receiverDocumentNumberType","payerName":"payerName","receiverBranchNumber":"receiverBranchNumber","paymentMethod":"paymentMethod","receiverRoutingNumberISPB":"receiverRoutingNumberISPB","payerBranchNumber":"payerBranchNumber"},"creditCardMetadata":{"installmentNumber":6.027456183070403,"totalInstallments":1.4658129805029452,"totalAmount":5.962133916683182,"billId":"billId","payeeMCC":5.637376656633329,"cardNumber":"cardNumber"},"categoryId":"categoryId","workspaceId":"workspaceId","status":"status"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/bank/transactions/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_transactions_controller_get_bank_transactions(client):
    """Test case for bank_transactions_controller_get_bank_transactions

    
    """
    params = [('pageIndex', 3.4),
                    ('pageSize', 3.4),
                    ('accountIds', 'account_ids_example'),
                    ('categoryIds', 'category_ids_example'),
                    ('tagIds', 'tag_ids_example'),
                    ('legalNatures', 'legal_natures_example'),
                    ('types', 'types_example'),
                    ('minPostedDate', 'min_posted_date_example'),
                    ('maxPostedDate', 'max_posted_date_example'),
                    ('minCompetencyDate', 'min_competency_date_example'),
                    ('maxCompetencyDate', 'max_competency_date_example'),
                    ('showIgnored', True),
                    ('ignoreAutomaticApplicationRelated', True),
                    ('ignoreInternalTransfers', True),
                    ('ignoreInvoiceRelated', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/bank/transactions'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_transactions_controller_get_bank_transactions_confirmed_today_by_me(client):
    """Test case for bank_transactions_controller_get_bank_transactions_confirmed_today_by_me

    
    """
    params = [('pageIndex', 3.4),
                    ('pageSize', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/bank/transactions/confirmed-today-by-me'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_transactions_controller_get_bank_transactions_not_confirmed(client):
    """Test case for bank_transactions_controller_get_bank_transactions_not_confirmed

    
    """
    params = [('pageIndex', 3.4),
                    ('pageSize', 3.4),
                    ('considerIgnored', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/bank/transactions/not-confirmed'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_transactions_controller_get_bank_transactions_totals(client):
    """Test case for bank_transactions_controller_get_bank_transactions_totals

    
    """
    params = [('accountIds', 'account_ids_example'),
                    ('categoryIds', 'category_ids_example'),
                    ('tagIds', 'tag_ids_example'),
                    ('legalNatures', 'legal_natures_example'),
                    ('minPostedDate', 'min_posted_date_example'),
                    ('maxPostedDate', 'max_posted_date_example'),
                    ('minCompetencyDate', 'min_competency_date_example'),
                    ('maxCompetencyDate', 'max_competency_date_example'),
                    ('showIgnored', True),
                    ('ignoreAutomaticApplicationRelated', True),
                    ('ignoreInternalTransfers', True),
                    ('ignoreInvoiceRelated', True),
                    ('types', 'types_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/bank/transactions/totals'.format(workspace_id='workspace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_transactions_controller_get_recent(client):
    """Test case for bank_transactions_controller_get_recent

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/workspaces/{workspace_id}/bank/transactions/most-recent'.format(workspace_id='workspace_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_transactions_controller_get_transaction_details(client):
    """Test case for bank_transactions_controller_get_transaction_details

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/bank/transactions/{bank_transaction_id}'.format(bank_transaction_id='bank_transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_transactions_controller_update_transaction(client):
    """Test case for bank_transactions_controller_update_transaction

    
    """
    body = {"confirm":True,"competencyDate":"2000-01-23T04:56:07.000+00:00","tagIds":["tagIds","tagIds"],"legalNature":"legalNature","description":"description","ignore":True,"categoryId":"categoryId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/bank/transactions/{bank_transaction_id}'.format(bank_transaction_id='bank_transaction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

