# python_core_api_sdk.BankTransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_transactions_controller_create_or_update_in_bulk**](BankTransactionsApi.md#bank_transactions_controller_create_or_update_in_bulk) | **PUT** /bank/transactions/bulk | 
[**bank_transactions_controller_get_by_id**](BankTransactionsApi.md#bank_transactions_controller_get_by_id) | **GET** /bank/transactions/{bankTransactionId} | 
[**bank_transactions_controller_get_by_provider**](BankTransactionsApi.md#bank_transactions_controller_get_by_provider) | **GET** /bank/accounts/{accountId}/transactions/by-provider | 
[**bank_transactions_controller_get_totals**](BankTransactionsApi.md#bank_transactions_controller_get_totals) | **GET** /bank/workspaces/{workspaceId}/transactions/totals | 
[**bank_transactions_controller_list**](BankTransactionsApi.md#bank_transactions_controller_list) | **GET** /bank/workspaces/{workspaceId}/transactions | 
[**bank_transactions_controller_list_most_recent**](BankTransactionsApi.md#bank_transactions_controller_list_most_recent) | **GET** /bank/workspaces/{workspaceId}/transactions/most-recent | 
[**bank_transactions_controller_list_not_verified**](BankTransactionsApi.md#bank_transactions_controller_list_not_verified) | **GET** /bank/workspaces/{workspaceId}/transactions/not-verified | 
[**bank_transactions_controller_list_verified_by_me**](BankTransactionsApi.md#bank_transactions_controller_list_verified_by_me) | **GET** /bank/workspaces/{workspaceId}/transactions/verified-by-me | 
[**bank_transactions_controller_partial_update**](BankTransactionsApi.md#bank_transactions_controller_partial_update) | **PATCH** /bank/transactions/{bankTransactionId} | 


# **bank_transactions_controller_create_or_update_in_bulk**
> List[BankTransactionEntity] bank_transactions_controller_create_or_update_in_bulk(create_or_update_bank_transactions_in_bulk_request_dto)



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
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    create_or_update_bank_transactions_in_bulk_request_dto = python_core_api_sdk.CreateOrUpdateBankTransactionsInBulkRequestDto() # CreateOrUpdateBankTransactionsInBulkRequestDto | 

    try:
        api_response = await api_instance.bank_transactions_controller_create_or_update_in_bulk(create_or_update_bank_transactions_in_bulk_request_dto)
        print("The response of BankTransactionsApi->bank_transactions_controller_create_or_update_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_create_or_update_in_bulk: %s\n" % e)
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

# **bank_transactions_controller_get_by_id**
> BankTransactionEntity bank_transactions_controller_get_by_id(bank_transaction_id)



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
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    bank_transaction_id = 'bank_transaction_id_example' # str | 

    try:
        api_response = await api_instance.bank_transactions_controller_get_by_id(bank_transaction_id)
        print("The response of BankTransactionsApi->bank_transactions_controller_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_get_by_id: %s\n" % e)
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

# **bank_transactions_controller_get_by_provider**
> BankTransactionEntity bank_transactions_controller_get_by_provider(account_id, provider, provider_transaction_id)



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
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    account_id = 'account_id_example' # str | 
    provider = 'provider_example' # str | 
    provider_transaction_id = 'provider_transaction_id_example' # str | 

    try:
        api_response = await api_instance.bank_transactions_controller_get_by_provider(account_id, provider, provider_transaction_id)
        print("The response of BankTransactionsApi->bank_transactions_controller_get_by_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_get_by_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **provider** | **str**|  | 
 **provider_transaction_id** | **str**|  | 

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

# **bank_transactions_controller_get_totals**
> BankTransactionsPageEntity bank_transactions_controller_get_totals(workspace_id, account_ids=account_ids, category_ids=category_ids, tag_ids=tag_ids, legal_natures=legal_natures, direction_natures=direction_natures, min_posted_datetime=min_posted_datetime, max_posted_datetime=max_posted_datetime, min_competency_datetime=min_competency_datetime, max_competency_datetime=max_competency_datetime, consider_ignored=consider_ignored, consider_automatic_application_related=consider_automatic_application_related, consider_internal_transfers=consider_internal_transfers, consider_invoice_related=consider_invoice_related)



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
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    account_ids = 'account_ids_example' # str |  (optional)
    category_ids = 'category_ids_example' # str |  (optional)
    tag_ids = 'tag_ids_example' # str |  (optional)
    legal_natures = 'legal_natures_example' # str |  (optional)
    direction_natures = 'direction_natures_example' # str |  (optional)
    min_posted_datetime = 'min_posted_datetime_example' # str |  (optional)
    max_posted_datetime = 'max_posted_datetime_example' # str |  (optional)
    min_competency_datetime = 'min_competency_datetime_example' # str |  (optional)
    max_competency_datetime = 'max_competency_datetime_example' # str |  (optional)
    consider_ignored = True # bool |  (optional)
    consider_automatic_application_related = True # bool |  (optional)
    consider_internal_transfers = True # bool |  (optional)
    consider_invoice_related = 'consider_invoice_related_example' # str |  (optional)

    try:
        api_response = await api_instance.bank_transactions_controller_get_totals(workspace_id, account_ids=account_ids, category_ids=category_ids, tag_ids=tag_ids, legal_natures=legal_natures, direction_natures=direction_natures, min_posted_datetime=min_posted_datetime, max_posted_datetime=max_posted_datetime, min_competency_datetime=min_competency_datetime, max_competency_datetime=max_competency_datetime, consider_ignored=consider_ignored, consider_automatic_application_related=consider_automatic_application_related, consider_internal_transfers=consider_internal_transfers, consider_invoice_related=consider_invoice_related)
        print("The response of BankTransactionsApi->bank_transactions_controller_get_totals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_get_totals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **account_ids** | **str**|  | [optional] 
 **category_ids** | **str**|  | [optional] 
 **tag_ids** | **str**|  | [optional] 
 **legal_natures** | **str**|  | [optional] 
 **direction_natures** | **str**|  | [optional] 
 **min_posted_datetime** | **str**|  | [optional] 
 **max_posted_datetime** | **str**|  | [optional] 
 **min_competency_datetime** | **str**|  | [optional] 
 **max_competency_datetime** | **str**|  | [optional] 
 **consider_ignored** | **bool**|  | [optional] 
 **consider_automatic_application_related** | **bool**|  | [optional] 
 **consider_internal_transfers** | **bool**|  | [optional] 
 **consider_invoice_related** | **str**|  | [optional] 

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

# **bank_transactions_controller_list**
> BankTransactionsPageEntity bank_transactions_controller_list(workspace_id, page_index=page_index, page_size=page_size, account_ids=account_ids, category_ids=category_ids, tag_ids=tag_ids, legal_natures=legal_natures, direction_natures=direction_natures, min_posted_datetime=min_posted_datetime, max_posted_datetime=max_posted_datetime, min_competency_datetime=min_competency_datetime, max_competency_datetime=max_competency_datetime, consider_ignored=consider_ignored, consider_automatic_application_related=consider_automatic_application_related, consider_internal_transfers=consider_internal_transfers, consider_invoice_related=consider_invoice_related)



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
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    page_index = 3.4 # float |  (optional)
    page_size = 3.4 # float |  (optional)
    account_ids = 'account_ids_example' # str |  (optional)
    category_ids = 'category_ids_example' # str |  (optional)
    tag_ids = 'tag_ids_example' # str |  (optional)
    legal_natures = 'legal_natures_example' # str |  (optional)
    direction_natures = 'direction_natures_example' # str |  (optional)
    min_posted_datetime = 'min_posted_datetime_example' # str |  (optional)
    max_posted_datetime = 'max_posted_datetime_example' # str |  (optional)
    min_competency_datetime = 'min_competency_datetime_example' # str |  (optional)
    max_competency_datetime = 'max_competency_datetime_example' # str |  (optional)
    consider_ignored = True # bool |  (optional)
    consider_automatic_application_related = True # bool |  (optional)
    consider_internal_transfers = True # bool |  (optional)
    consider_invoice_related = 'consider_invoice_related_example' # str |  (optional)

    try:
        api_response = await api_instance.bank_transactions_controller_list(workspace_id, page_index=page_index, page_size=page_size, account_ids=account_ids, category_ids=category_ids, tag_ids=tag_ids, legal_natures=legal_natures, direction_natures=direction_natures, min_posted_datetime=min_posted_datetime, max_posted_datetime=max_posted_datetime, min_competency_datetime=min_competency_datetime, max_competency_datetime=max_competency_datetime, consider_ignored=consider_ignored, consider_automatic_application_related=consider_automatic_application_related, consider_internal_transfers=consider_internal_transfers, consider_invoice_related=consider_invoice_related)
        print("The response of BankTransactionsApi->bank_transactions_controller_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_list: %s\n" % e)
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
 **direction_natures** | **str**|  | [optional] 
 **min_posted_datetime** | **str**|  | [optional] 
 **max_posted_datetime** | **str**|  | [optional] 
 **min_competency_datetime** | **str**|  | [optional] 
 **max_competency_datetime** | **str**|  | [optional] 
 **consider_ignored** | **bool**|  | [optional] 
 **consider_automatic_application_related** | **bool**|  | [optional] 
 **consider_internal_transfers** | **bool**|  | [optional] 
 **consider_invoice_related** | **str**|  | [optional] 

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

# **bank_transactions_controller_list_most_recent**
> List[BankTransactionEntity] bank_transactions_controller_list_most_recent(workspace_id)



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
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        api_response = await api_instance.bank_transactions_controller_list_most_recent(workspace_id)
        print("The response of BankTransactionsApi->bank_transactions_controller_list_most_recent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_list_most_recent: %s\n" % e)
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

# **bank_transactions_controller_list_not_verified**
> BankTransactionsPageEntity bank_transactions_controller_list_not_verified(workspace_id, page_index=page_index, page_size=page_size, consider_ignored=consider_ignored)



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
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    page_index = 3.4 # float |  (optional)
    page_size = 3.4 # float |  (optional)
    consider_ignored = True # bool |  (optional)

    try:
        api_response = await api_instance.bank_transactions_controller_list_not_verified(workspace_id, page_index=page_index, page_size=page_size, consider_ignored=consider_ignored)
        print("The response of BankTransactionsApi->bank_transactions_controller_list_not_verified:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_list_not_verified: %s\n" % e)
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

# **bank_transactions_controller_list_verified_by_me**
> BankTransactionsPageEntity bank_transactions_controller_list_verified_by_me(workspace_id, from_datetime, to_datetime, page_index=page_index, page_size=page_size)



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
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    from_datetime = 'from_datetime_example' # str | 
    to_datetime = 'to_datetime_example' # str | 
    page_index = 3.4 # float |  (optional)
    page_size = 3.4 # float |  (optional)

    try:
        api_response = await api_instance.bank_transactions_controller_list_verified_by_me(workspace_id, from_datetime, to_datetime, page_index=page_index, page_size=page_size)
        print("The response of BankTransactionsApi->bank_transactions_controller_list_verified_by_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_list_verified_by_me: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **from_datetime** | **str**|  | 
 **to_datetime** | **str**|  | 
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

# **bank_transactions_controller_partial_update**
> BankTransactionEntity bank_transactions_controller_partial_update(bank_transaction_id, partial_update_bank_transaction_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_transaction_entity import BankTransactionEntity
from python_core_api_sdk.models.partial_update_bank_transaction_request_dto import PartialUpdateBankTransactionRequestDto
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.BankTransactionsApi(api_client)
    bank_transaction_id = 'bank_transaction_id_example' # str | 
    partial_update_bank_transaction_request_dto = python_core_api_sdk.PartialUpdateBankTransactionRequestDto() # PartialUpdateBankTransactionRequestDto | 

    try:
        api_response = await api_instance.bank_transactions_controller_partial_update(bank_transaction_id, partial_update_bank_transaction_request_dto)
        print("The response of BankTransactionsApi->bank_transactions_controller_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transactions_controller_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transaction_id** | **str**|  | 
 **partial_update_bank_transaction_request_dto** | [**PartialUpdateBankTransactionRequestDto**](PartialUpdateBankTransactionRequestDto.md)|  | 

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

