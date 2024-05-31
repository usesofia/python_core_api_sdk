# python_core_api_sdk.BankTransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_transactions_controller_create_or_update_bank_transactions_in_bulk**](BankTransactionsApi.md#bank_transactions_controller_create_or_update_bank_transactions_in_bulk) | **PUT** /bank/transactions/bulk | 
[**bank_transactions_controller_get_bank_transactions**](BankTransactionsApi.md#bank_transactions_controller_get_bank_transactions) | **GET** /workspaces/{workspaceId}/bank/transactions | 
[**bank_transactions_controller_get_bank_transactions_confirmed_today_by_me**](BankTransactionsApi.md#bank_transactions_controller_get_bank_transactions_confirmed_today_by_me) | **GET** /workspaces/{workspaceId}/bank/transactions/confirmed-today-by-me | 
[**bank_transactions_controller_get_bank_transactions_not_confirmed**](BankTransactionsApi.md#bank_transactions_controller_get_bank_transactions_not_confirmed) | **GET** /workspaces/{workspaceId}/bank/transactions/not-confirmed | 
[**bank_transactions_controller_get_bank_transactions_totals**](BankTransactionsApi.md#bank_transactions_controller_get_bank_transactions_totals) | **GET** /workspaces/{workspaceId}/bank/transactions/totals | 
[**bank_transactions_controller_get_recent**](BankTransactionsApi.md#bank_transactions_controller_get_recent) | **GET** /workspaces/{workspaceId}/bank/transactions/most-recent | 
[**bank_transactions_controller_get_transaction_details**](BankTransactionsApi.md#bank_transactions_controller_get_transaction_details) | **GET** /bank/transactions/{bankTransactionId} | 
[**bank_transactions_controller_update_transaction**](BankTransactionsApi.md#bank_transactions_controller_update_transaction) | **PATCH** /bank/transactions/{bankTransactionId} | 


# **bank_transactions_controller_create_or_update_bank_transactions_in_bulk**
> List[BankTransactionEntity] bank_transactions_controller_create_or_update_bank_transactions_in_bulk(create_or_update_bank_transactions_in_bulk_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_transaction_entity import BankTransactionEntity
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto import CreateOrUpdateBankTransactionsInBulkRequestDto
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
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    create_or_update_bank_transactions_in_bulk_request_dto = python_core_api_sdk.CreateOrUpdateBankTransactionsInBulkRequestDto() # CreateOrUpdateBankTransactionsInBulkRequestDto | 

    try:
        api_response = api_instance.bank_transactions_controller_create_or_update_bank_transactions_in_bulk(create_or_update_bank_transactions_in_bulk_request_dto)
        print("The response of BankTransactionsApi->bank_transactions_controller_create_or_update_bank_transactions_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_create_or_update_bank_transactions_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_or_update_bank_transactions_in_bulk_request_dto** | [**CreateOrUpdateBankTransactionsInBulkRequestDto**](CreateOrUpdateBankTransactionsInBulkRequestDto.md)|  | 

### Return type

[**List[BankTransactionEntity]**](BankTransactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_transactions_controller_get_bank_transactions**
> BankTransactionsPageEntity bank_transactions_controller_get_bank_transactions(workspace_id, page_index=page_index, page_size=page_size, account_ids=account_ids, category_ids=category_ids, tag_ids=tag_ids, legal_natures=legal_natures, types=types, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date, show_ignored=show_ignored, ignore_automatic_application_related=ignore_automatic_application_related, ignore_internal_transfers=ignore_internal_transfers, ignore_invoice_related=ignore_invoice_related)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_transactions_page_entity import BankTransactionsPageEntity
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
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    page_index = 3.4 # float |  (optional)
    page_size = 3.4 # float |  (optional)
    account_ids = 'account_ids_example' # str |  (optional)
    category_ids = 'category_ids_example' # str |  (optional)
    tag_ids = 'tag_ids_example' # str |  (optional)
    legal_natures = 'legal_natures_example' # str |  (optional)
    types = 'types_example' # str |  (optional)
    min_posted_date = 'min_posted_date_example' # str |  (optional)
    max_posted_date = 'max_posted_date_example' # str |  (optional)
    min_competency_date = 'min_competency_date_example' # str |  (optional)
    max_competency_date = 'max_competency_date_example' # str |  (optional)
    show_ignored = True # bool |  (optional)
    ignore_automatic_application_related = True # bool |  (optional)
    ignore_internal_transfers = True # bool |  (optional)
    ignore_invoice_related = True # bool |  (optional)

    try:
        api_response = api_instance.bank_transactions_controller_get_bank_transactions(workspace_id, page_index=page_index, page_size=page_size, account_ids=account_ids, category_ids=category_ids, tag_ids=tag_ids, legal_natures=legal_natures, types=types, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date, show_ignored=show_ignored, ignore_automatic_application_related=ignore_automatic_application_related, ignore_internal_transfers=ignore_internal_transfers, ignore_invoice_related=ignore_invoice_related)
        print("The response of BankTransactionsApi->bank_transactions_controller_get_bank_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_get_bank_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **page_index** | **float**|  | [optional] 
 **page_size** | **float**|  | [optional] 
 **account_ids** | **str**|  | [optional] 
 **category_ids** | **str**|  | [optional] 
 **tag_ids** | **str**|  | [optional] 
 **legal_natures** | **str**|  | [optional] 
 **types** | **str**|  | [optional] 
 **min_posted_date** | **str**|  | [optional] 
 **max_posted_date** | **str**|  | [optional] 
 **min_competency_date** | **str**|  | [optional] 
 **max_competency_date** | **str**|  | [optional] 
 **show_ignored** | **bool**|  | [optional] 
 **ignore_automatic_application_related** | **bool**|  | [optional] 
 **ignore_internal_transfers** | **bool**|  | [optional] 
 **ignore_invoice_related** | **bool**|  | [optional] 

### Return type

[**BankTransactionsPageEntity**](BankTransactionsPageEntity.md)

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

# **bank_transactions_controller_get_bank_transactions_confirmed_today_by_me**
> BankTransactionsPageEntity bank_transactions_controller_get_bank_transactions_confirmed_today_by_me(workspace_id, page_index=page_index, page_size=page_size)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_transactions_page_entity import BankTransactionsPageEntity
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
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    page_index = 3.4 # float |  (optional)
    page_size = 3.4 # float |  (optional)

    try:
        api_response = api_instance.bank_transactions_controller_get_bank_transactions_confirmed_today_by_me(workspace_id, page_index=page_index, page_size=page_size)
        print("The response of BankTransactionsApi->bank_transactions_controller_get_bank_transactions_confirmed_today_by_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_get_bank_transactions_confirmed_today_by_me: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **page_index** | **float**|  | [optional] 
 **page_size** | **float**|  | [optional] 

### Return type

[**BankTransactionsPageEntity**](BankTransactionsPageEntity.md)

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

# **bank_transactions_controller_get_bank_transactions_not_confirmed**
> BankTransactionsPageEntity bank_transactions_controller_get_bank_transactions_not_confirmed(workspace_id, page_index=page_index, page_size=page_size, consider_ignored=consider_ignored)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_transactions_page_entity import BankTransactionsPageEntity
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
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    page_index = 3.4 # float |  (optional)
    page_size = 3.4 # float |  (optional)
    consider_ignored = True # bool |  (optional)

    try:
        api_response = api_instance.bank_transactions_controller_get_bank_transactions_not_confirmed(workspace_id, page_index=page_index, page_size=page_size, consider_ignored=consider_ignored)
        print("The response of BankTransactionsApi->bank_transactions_controller_get_bank_transactions_not_confirmed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_get_bank_transactions_not_confirmed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **page_index** | **float**|  | [optional] 
 **page_size** | **float**|  | [optional] 
 **consider_ignored** | **bool**|  | [optional] 

### Return type

[**BankTransactionsPageEntity**](BankTransactionsPageEntity.md)

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

# **bank_transactions_controller_get_bank_transactions_totals**
> BankTransactionsPageEntity bank_transactions_controller_get_bank_transactions_totals(workspace_id, account_ids=account_ids, category_ids=category_ids, tag_ids=tag_ids, legal_natures=legal_natures, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date, show_ignored=show_ignored, ignore_automatic_application_related=ignore_automatic_application_related, ignore_internal_transfers=ignore_internal_transfers, ignore_invoice_related=ignore_invoice_related, types=types)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_transactions_page_entity import BankTransactionsPageEntity
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
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    account_ids = 'account_ids_example' # str |  (optional)
    category_ids = 'category_ids_example' # str |  (optional)
    tag_ids = 'tag_ids_example' # str |  (optional)
    legal_natures = 'legal_natures_example' # str |  (optional)
    min_posted_date = 'min_posted_date_example' # str |  (optional)
    max_posted_date = 'max_posted_date_example' # str |  (optional)
    min_competency_date = 'min_competency_date_example' # str |  (optional)
    max_competency_date = 'max_competency_date_example' # str |  (optional)
    show_ignored = True # bool |  (optional)
    ignore_automatic_application_related = True # bool |  (optional)
    ignore_internal_transfers = True # bool |  (optional)
    ignore_invoice_related = True # bool |  (optional)
    types = 'types_example' # str |  (optional)

    try:
        api_response = api_instance.bank_transactions_controller_get_bank_transactions_totals(workspace_id, account_ids=account_ids, category_ids=category_ids, tag_ids=tag_ids, legal_natures=legal_natures, min_posted_date=min_posted_date, max_posted_date=max_posted_date, min_competency_date=min_competency_date, max_competency_date=max_competency_date, show_ignored=show_ignored, ignore_automatic_application_related=ignore_automatic_application_related, ignore_internal_transfers=ignore_internal_transfers, ignore_invoice_related=ignore_invoice_related, types=types)
        print("The response of BankTransactionsApi->bank_transactions_controller_get_bank_transactions_totals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_get_bank_transactions_totals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **account_ids** | **str**|  | [optional] 
 **category_ids** | **str**|  | [optional] 
 **tag_ids** | **str**|  | [optional] 
 **legal_natures** | **str**|  | [optional] 
 **min_posted_date** | **str**|  | [optional] 
 **max_posted_date** | **str**|  | [optional] 
 **min_competency_date** | **str**|  | [optional] 
 **max_competency_date** | **str**|  | [optional] 
 **show_ignored** | **bool**|  | [optional] 
 **ignore_automatic_application_related** | **bool**|  | [optional] 
 **ignore_internal_transfers** | **bool**|  | [optional] 
 **ignore_invoice_related** | **bool**|  | [optional] 
 **types** | **str**|  | [optional] 

### Return type

[**BankTransactionsPageEntity**](BankTransactionsPageEntity.md)

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

# **bank_transactions_controller_get_recent**
> List[BankTransactionEntity] bank_transactions_controller_get_recent(workspace_id)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_transaction_entity import BankTransactionEntity
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
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        api_response = api_instance.bank_transactions_controller_get_recent(workspace_id)
        print("The response of BankTransactionsApi->bank_transactions_controller_get_recent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_get_recent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[BankTransactionEntity]**](BankTransactionEntity.md)

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

# **bank_transactions_controller_get_transaction_details**
> BankTransactionEntity bank_transactions_controller_get_transaction_details(bank_transaction_id)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_transaction_entity import BankTransactionEntity
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
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    bank_transaction_id = 'bank_transaction_id_example' # str | 

    try:
        api_response = api_instance.bank_transactions_controller_get_transaction_details(bank_transaction_id)
        print("The response of BankTransactionsApi->bank_transactions_controller_get_transaction_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_get_transaction_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transaction_id** | **str**|  | 

### Return type

[**BankTransactionEntity**](BankTransactionEntity.md)

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

# **bank_transactions_controller_update_transaction**
> BankTransactionEntity bank_transactions_controller_update_transaction(bank_transaction_id, update_bank_transaction_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_transaction_entity import BankTransactionEntity
from python_core_api_sdk.models.update_bank_transaction_request_dto import UpdateBankTransactionRequestDto
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
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    bank_transaction_id = 'bank_transaction_id_example' # str | 
    update_bank_transaction_request_dto = python_core_api_sdk.UpdateBankTransactionRequestDto() # UpdateBankTransactionRequestDto | 

    try:
        api_response = api_instance.bank_transactions_controller_update_transaction(bank_transaction_id, update_bank_transaction_request_dto)
        print("The response of BankTransactionsApi->bank_transactions_controller_update_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_update_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transaction_id** | **str**|  | 
 **update_bank_transaction_request_dto** | [**UpdateBankTransactionRequestDto**](UpdateBankTransactionRequestDto.md)|  | 

### Return type

[**BankTransactionEntity**](BankTransactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

