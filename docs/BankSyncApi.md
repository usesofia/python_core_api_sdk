# python_core_api_sdk.BankSyncApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_sync_controller_sync_account_transactions**](BankSyncApi.md#bank_sync_controller_sync_account_transactions) | **POST** /bank/sync/transactions | 
[**bank_sync_controller_sync_item**](BankSyncApi.md#bank_sync_controller_sync_item) | **POST** /bank/sync/items | 
[**bank_sync_controller_sync_transactions_page_begin**](BankSyncApi.md#bank_sync_controller_sync_transactions_page_begin) | **POST** /bank/sync/transactions/page/begin | 
[**bank_sync_controller_sync_transactions_page_end**](BankSyncApi.md#bank_sync_controller_sync_transactions_page_end) | **POST** /bank/sync/transactions/page/end | 


# **bank_sync_controller_sync_account_transactions**
> bank_sync_controller_sync_account_transactions(sync_bank_account_transactions_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.sync_bank_account_transactions_request_dto import SyncBankAccountTransactionsRequestDto
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
    api_instance = python_core_api_sdk.BankSyncApi(api_client)
    sync_bank_account_transactions_request_dto = python_core_api_sdk.SyncBankAccountTransactionsRequestDto() # SyncBankAccountTransactionsRequestDto | 

    try:
        await api_instance.bank_sync_controller_sync_account_transactions(sync_bank_account_transactions_request_dto)
    except Exception as e:
        print("Exception when calling BankSyncApi->bank_sync_controller_sync_account_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_bank_account_transactions_request_dto** | [**SyncBankAccountTransactionsRequestDto**](SyncBankAccountTransactionsRequestDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_sync_controller_sync_item**
> bank_sync_controller_sync_item(sync_bank_item_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.sync_bank_item_request_dto import SyncBankItemRequestDto
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
    api_instance = python_core_api_sdk.BankSyncApi(api_client)
    sync_bank_item_request_dto = python_core_api_sdk.SyncBankItemRequestDto() # SyncBankItemRequestDto | 

    try:
        await api_instance.bank_sync_controller_sync_item(sync_bank_item_request_dto)
    except Exception as e:
        print("Exception when calling BankSyncApi->bank_sync_controller_sync_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_bank_item_request_dto** | [**SyncBankItemRequestDto**](SyncBankItemRequestDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_sync_controller_sync_transactions_page_begin**
> bank_sync_controller_sync_transactions_page_begin(sync_bank_account_transactions_page_begin_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.sync_bank_account_transactions_page_begin_request_dto import SyncBankAccountTransactionsPageBeginRequestDto
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
    api_instance = python_core_api_sdk.BankSyncApi(api_client)
    sync_bank_account_transactions_page_begin_request_dto = python_core_api_sdk.SyncBankAccountTransactionsPageBeginRequestDto() # SyncBankAccountTransactionsPageBeginRequestDto | 

    try:
        await api_instance.bank_sync_controller_sync_transactions_page_begin(sync_bank_account_transactions_page_begin_request_dto)
    except Exception as e:
        print("Exception when calling BankSyncApi->bank_sync_controller_sync_transactions_page_begin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_bank_account_transactions_page_begin_request_dto** | [**SyncBankAccountTransactionsPageBeginRequestDto**](SyncBankAccountTransactionsPageBeginRequestDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_sync_controller_sync_transactions_page_end**
> bank_sync_controller_sync_transactions_page_end(sync_bank_account_transactions_page_end_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto import SyncBankAccountTransactionsPageEndRequestDto
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
    api_instance = python_core_api_sdk.BankSyncApi(api_client)
    sync_bank_account_transactions_page_end_request_dto = python_core_api_sdk.SyncBankAccountTransactionsPageEndRequestDto() # SyncBankAccountTransactionsPageEndRequestDto | 

    try:
        await api_instance.bank_sync_controller_sync_transactions_page_end(sync_bank_account_transactions_page_end_request_dto)
    except Exception as e:
        print("Exception when calling BankSyncApi->bank_sync_controller_sync_transactions_page_end: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_bank_account_transactions_page_end_request_dto** | [**SyncBankAccountTransactionsPageEndRequestDto**](SyncBankAccountTransactionsPageEndRequestDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

