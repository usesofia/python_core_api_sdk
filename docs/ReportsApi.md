# python_core_api_sdk.ReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_controller_get_accounts_entries_by_category_report**](ReportsApi.md#reports_controller_get_accounts_entries_by_category_report) | **GET** /workspaces/{workspaceId}/reports/accounts/entries-by-category | 
[**reports_controller_get_accounts_outputs_by_category_report**](ReportsApi.md#reports_controller_get_accounts_outputs_by_category_report) | **GET** /workspaces/{workspaceId}/reports/accounts/outputs-by-category | 
[**reports_controller_get_business_indicators**](ReportsApi.md#reports_controller_get_business_indicators) | **GET** /workspaces/{workspaceId}/reports/indicators/business | 
[**reports_controller_get_cards_cash_flow_report**](ReportsApi.md#reports_controller_get_cards_cash_flow_report) | **GET** /workspaces/{workspaceId}/reports/cards/cash-flow | 
[**reports_controller_get_cards_outputs_by_category_report**](ReportsApi.md#reports_controller_get_cards_outputs_by_category_report) | **GET** /workspaces/{workspaceId}/reports/cards/outputs-by-category | 
[**reports_controller_get_cash_flow_report**](ReportsApi.md#reports_controller_get_cash_flow_report) | **GET** /workspaces/{workspaceId}/reports/accounts/cash-flow | 
[**reports_controller_get_financial_statement_report**](ReportsApi.md#reports_controller_get_financial_statement_report) | **GET** /workspaces/{workspaceId}/reports/financial-statement | 


# **reports_controller_get_accounts_entries_by_category_report**
> CashFlowByCategoryReportEntity reports_controller_get_accounts_entries_by_category_report(workspace_id, account_ids=account_ids, tag_ids=tag_ids, legal_natures=legal_natures, consider_ignored=consider_ignored, ignore_internal_transfers=ignore_internal_transfers, ignore_automatic_application_related=ignore_automatic_application_related, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.cash_flow_by_category_report_entity import CashFlowByCategoryReportEntity
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.ReportsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    account_ids = 'account_ids_example' # str |  (optional)
    tag_ids = 'tag_ids_example' # str |  (optional)
    legal_natures = 'legal_natures_example' # str |  (optional)
    consider_ignored = True # bool |  (optional)
    ignore_internal_transfers = True # bool |  (optional)
    ignore_automatic_application_related = True # bool |  (optional)
    min_posted_date = 'min_posted_date_example' # str |  (optional)
    max_posted_date = 'max_posted_date_example' # str |  (optional)
    min_competency_date = 'min_competency_date_example' # str |  (optional)
    max_competency_date = 'max_competency_date_example' # str |  (optional)

    try:
        api_response = api_instance.reports_controller_get_accounts_entries_by_category_report(workspace_id, account_ids=account_ids, tag_ids=tag_ids, legal_natures=legal_natures, consider_ignored=consider_ignored, ignore_internal_transfers=ignore_internal_transfers, ignore_automatic_application_related=ignore_automatic_application_related, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date)
        print("The response of ReportsApi->reports_controller_get_accounts_entries_by_category_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->reports_controller_get_accounts_entries_by_category_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **account_ids** | **str**|  | [optional] 
 **tag_ids** | **str**|  | [optional] 
 **legal_natures** | **str**|  | [optional] 
 **consider_ignored** | **bool**|  | [optional] 
 **ignore_internal_transfers** | **bool**|  | [optional] 
 **ignore_automatic_application_related** | **bool**|  | [optional] 
 **min_posted_date** | **str**|  | [optional] 
 **max_posted_date** | **str**|  | [optional] 
 **min_competency_date** | **str**|  | [optional] 
 **max_competency_date** | **str**|  | [optional] 

### Return type

[**CashFlowByCategoryReportEntity**](CashFlowByCategoryReportEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_controller_get_accounts_outputs_by_category_report**
> CashFlowByCategoryReportEntity reports_controller_get_accounts_outputs_by_category_report(workspace_id, account_ids=account_ids, tag_ids=tag_ids, legal_natures=legal_natures, consider_ignored=consider_ignored, ignore_internal_transfers=ignore_internal_transfers, ignore_automatic_application_related=ignore_automatic_application_related, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.cash_flow_by_category_report_entity import CashFlowByCategoryReportEntity
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.ReportsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    account_ids = 'account_ids_example' # str |  (optional)
    tag_ids = 'tag_ids_example' # str |  (optional)
    legal_natures = 'legal_natures_example' # str |  (optional)
    consider_ignored = True # bool |  (optional)
    ignore_internal_transfers = True # bool |  (optional)
    ignore_automatic_application_related = True # bool |  (optional)
    min_posted_date = 'min_posted_date_example' # str |  (optional)
    max_posted_date = 'max_posted_date_example' # str |  (optional)
    min_competency_date = 'min_competency_date_example' # str |  (optional)
    max_competency_date = 'max_competency_date_example' # str |  (optional)

    try:
        api_response = api_instance.reports_controller_get_accounts_outputs_by_category_report(workspace_id, account_ids=account_ids, tag_ids=tag_ids, legal_natures=legal_natures, consider_ignored=consider_ignored, ignore_internal_transfers=ignore_internal_transfers, ignore_automatic_application_related=ignore_automatic_application_related, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date)
        print("The response of ReportsApi->reports_controller_get_accounts_outputs_by_category_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->reports_controller_get_accounts_outputs_by_category_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **account_ids** | **str**|  | [optional] 
 **tag_ids** | **str**|  | [optional] 
 **legal_natures** | **str**|  | [optional] 
 **consider_ignored** | **bool**|  | [optional] 
 **ignore_internal_transfers** | **bool**|  | [optional] 
 **ignore_automatic_application_related** | **bool**|  | [optional] 
 **min_posted_date** | **str**|  | [optional] 
 **max_posted_date** | **str**|  | [optional] 
 **min_competency_date** | **str**|  | [optional] 
 **max_competency_date** | **str**|  | [optional] 

### Return type

[**CashFlowByCategoryReportEntity**](CashFlowByCategoryReportEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_controller_get_business_indicators**
> List[BankTransactionIndicatorEntity] reports_controller_get_business_indicators(workspace_id, account_ids=account_ids, tag_ids=tag_ids, consider_ignored=consider_ignored, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_transaction_indicator_entity import BankTransactionIndicatorEntity
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.ReportsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    account_ids = 'account_ids_example' # str |  (optional)
    tag_ids = 'tag_ids_example' # str |  (optional)
    consider_ignored = True # bool |  (optional)
    min_posted_date = 'min_posted_date_example' # str |  (optional)
    max_posted_date = 'max_posted_date_example' # str |  (optional)
    min_competency_date = 'min_competency_date_example' # str |  (optional)
    max_competency_date = 'max_competency_date_example' # str |  (optional)

    try:
        api_response = api_instance.reports_controller_get_business_indicators(workspace_id, account_ids=account_ids, tag_ids=tag_ids, consider_ignored=consider_ignored, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date)
        print("The response of ReportsApi->reports_controller_get_business_indicators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->reports_controller_get_business_indicators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **account_ids** | **str**|  | [optional] 
 **tag_ids** | **str**|  | [optional] 
 **consider_ignored** | **bool**|  | [optional] 
 **min_posted_date** | **str**|  | [optional] 
 **max_posted_date** | **str**|  | [optional] 
 **min_competency_date** | **str**|  | [optional] 
 **max_competency_date** | **str**|  | [optional] 

### Return type

[**List[BankTransactionIndicatorEntity]**](BankTransactionIndicatorEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_controller_get_cards_cash_flow_report**
> CashFlowReportEntity reports_controller_get_cards_cash_flow_report(workspace_id, account_ids=account_ids, category_ids=category_ids, tag_ids=tag_ids, legal_natures=legal_natures, consider_ignored=consider_ignored, ignore_invoice_related=ignore_invoice_related)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.cash_flow_report_entity import CashFlowReportEntity
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.ReportsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    account_ids = 'account_ids_example' # str |  (optional)
    category_ids = 'category_ids_example' # str |  (optional)
    tag_ids = 'tag_ids_example' # str |  (optional)
    legal_natures = 'legal_natures_example' # str |  (optional)
    consider_ignored = True # bool |  (optional)
    ignore_invoice_related = True # bool |  (optional)

    try:
        api_response = api_instance.reports_controller_get_cards_cash_flow_report(workspace_id, account_ids=account_ids, category_ids=category_ids, tag_ids=tag_ids, legal_natures=legal_natures, consider_ignored=consider_ignored, ignore_invoice_related=ignore_invoice_related)
        print("The response of ReportsApi->reports_controller_get_cards_cash_flow_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->reports_controller_get_cards_cash_flow_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **account_ids** | **str**|  | [optional] 
 **category_ids** | **str**|  | [optional] 
 **tag_ids** | **str**|  | [optional] 
 **legal_natures** | **str**|  | [optional] 
 **consider_ignored** | **bool**|  | [optional] 
 **ignore_invoice_related** | **bool**|  | [optional] 

### Return type

[**CashFlowReportEntity**](CashFlowReportEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_controller_get_cards_outputs_by_category_report**
> CashFlowByCategoryReportEntity reports_controller_get_cards_outputs_by_category_report(workspace_id, account_ids=account_ids, tag_ids=tag_ids, legal_natures=legal_natures, consider_ignored=consider_ignored, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date, ignore_invoice_related=ignore_invoice_related)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.cash_flow_by_category_report_entity import CashFlowByCategoryReportEntity
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.ReportsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    account_ids = 'account_ids_example' # str |  (optional)
    tag_ids = 'tag_ids_example' # str |  (optional)
    legal_natures = 'legal_natures_example' # str |  (optional)
    consider_ignored = True # bool |  (optional)
    min_posted_date = 'min_posted_date_example' # str |  (optional)
    max_posted_date = 'max_posted_date_example' # str |  (optional)
    min_competency_date = 'min_competency_date_example' # str |  (optional)
    max_competency_date = 'max_competency_date_example' # str |  (optional)
    ignore_invoice_related = True # bool |  (optional)

    try:
        api_response = api_instance.reports_controller_get_cards_outputs_by_category_report(workspace_id, account_ids=account_ids, tag_ids=tag_ids, legal_natures=legal_natures, consider_ignored=consider_ignored, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date, ignore_invoice_related=ignore_invoice_related)
        print("The response of ReportsApi->reports_controller_get_cards_outputs_by_category_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->reports_controller_get_cards_outputs_by_category_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **account_ids** | **str**|  | [optional] 
 **tag_ids** | **str**|  | [optional] 
 **legal_natures** | **str**|  | [optional] 
 **consider_ignored** | **bool**|  | [optional] 
 **min_posted_date** | **str**|  | [optional] 
 **max_posted_date** | **str**|  | [optional] 
 **min_competency_date** | **str**|  | [optional] 
 **max_competency_date** | **str**|  | [optional] 
 **ignore_invoice_related** | **bool**|  | [optional] 

### Return type

[**CashFlowByCategoryReportEntity**](CashFlowByCategoryReportEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_controller_get_cash_flow_report**
> CashFlowReportEntity reports_controller_get_cash_flow_report(workspace_id, account_ids=account_ids, category_ids=category_ids, tag_ids=tag_ids, legal_natures=legal_natures, consider_ignored=consider_ignored, ignore_internal_transfers=ignore_internal_transfers, ignore_automatic_application_related=ignore_automatic_application_related)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.cash_flow_report_entity import CashFlowReportEntity
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.ReportsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    account_ids = 'account_ids_example' # str |  (optional)
    category_ids = 'category_ids_example' # str |  (optional)
    tag_ids = 'tag_ids_example' # str |  (optional)
    legal_natures = 'legal_natures_example' # str |  (optional)
    consider_ignored = True # bool |  (optional)
    ignore_internal_transfers = True # bool |  (optional)
    ignore_automatic_application_related = True # bool |  (optional)

    try:
        api_response = api_instance.reports_controller_get_cash_flow_report(workspace_id, account_ids=account_ids, category_ids=category_ids, tag_ids=tag_ids, legal_natures=legal_natures, consider_ignored=consider_ignored, ignore_internal_transfers=ignore_internal_transfers, ignore_automatic_application_related=ignore_automatic_application_related)
        print("The response of ReportsApi->reports_controller_get_cash_flow_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->reports_controller_get_cash_flow_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **account_ids** | **str**|  | [optional] 
 **category_ids** | **str**|  | [optional] 
 **tag_ids** | **str**|  | [optional] 
 **legal_natures** | **str**|  | [optional] 
 **consider_ignored** | **bool**|  | [optional] 
 **ignore_internal_transfers** | **bool**|  | [optional] 
 **ignore_automatic_application_related** | **bool**|  | [optional] 

### Return type

[**CashFlowReportEntity**](CashFlowReportEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_controller_get_financial_statement_report**
> FinancialStatementReport reports_controller_get_financial_statement_report(workspace_id, account_ids=account_ids, tag_ids=tag_ids, legal_natures=legal_natures, consider_ignored=consider_ignored, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.financial_statement_report import FinancialStatementReport
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.ReportsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    account_ids = 'account_ids_example' # str |  (optional)
    tag_ids = 'tag_ids_example' # str |  (optional)
    legal_natures = 'legal_natures_example' # str |  (optional)
    consider_ignored = True # bool |  (optional)
    min_posted_date = 'min_posted_date_example' # str |  (optional)
    max_posted_date = 'max_posted_date_example' # str |  (optional)
    min_competency_date = 'min_competency_date_example' # str |  (optional)
    max_competency_date = 'max_competency_date_example' # str |  (optional)

    try:
        api_response = api_instance.reports_controller_get_financial_statement_report(workspace_id, account_ids=account_ids, tag_ids=tag_ids, legal_natures=legal_natures, consider_ignored=consider_ignored, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date)
        print("The response of ReportsApi->reports_controller_get_financial_statement_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->reports_controller_get_financial_statement_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **account_ids** | **str**|  | [optional] 
 **tag_ids** | **str**|  | [optional] 
 **legal_natures** | **str**|  | [optional] 
 **consider_ignored** | **bool**|  | [optional] 
 **min_posted_date** | **str**|  | [optional] 
 **max_posted_date** | **str**|  | [optional] 
 **min_competency_date** | **str**|  | [optional] 
 **max_competency_date** | **str**|  | [optional] 

### Return type

[**FinancialStatementReport**](FinancialStatementReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

