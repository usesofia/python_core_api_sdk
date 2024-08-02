# python_core_api_sdk.BankAccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_accounts_controller_activate**](BankAccountsApi.md#bank_accounts_controller_activate) | **POST** /bank/accounts/{bankAccountId}/activate | 
[**bank_accounts_controller_create_or_update**](BankAccountsApi.md#bank_accounts_controller_create_or_update) | **PUT** /bank/accounts | 
[**bank_accounts_controller_create_workspace_balance_report**](BankAccountsApi.md#bank_accounts_controller_create_workspace_balance_report) | **POST** /bank/workspaces/{workspaceId}/accounts/balance-report | 
[**bank_accounts_controller_disable**](BankAccountsApi.md#bank_accounts_controller_disable) | **POST** /bank/accounts/{bankAccountId}/disable | 
[**bank_accounts_controller_get_by_id**](BankAccountsApi.md#bank_accounts_controller_get_by_id) | **GET** /bank/accounts/{bankAccountId} | 
[**bank_accounts_controller_list_by_bank_connection_id**](BankAccountsApi.md#bank_accounts_controller_list_by_bank_connection_id) | **GET** /bank/connections/{bankConnectionId}/accounts | 
[**bank_accounts_controller_list_by_workspace_id**](BankAccountsApi.md#bank_accounts_controller_list_by_workspace_id) | **GET** /bank/workspaces/{workspaceId}/accounts | 


# **bank_accounts_controller_activate**
> BankAccountEntity bank_accounts_controller_activate(bank_account_id)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_account_entity import BankAccountEntity
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
    api_instance = python_core_api_sdk.BankAccountsApi(api_client)
    bank_account_id = 'bank_account_id_example' # str | 

    try:
        api_response = await api_instance.bank_accounts_controller_activate(bank_account_id)
        print("The response of BankAccountsApi->bank_accounts_controller_activate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->bank_accounts_controller_activate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**|  | 

### Return type

[**BankAccountEntity**](BankAccountEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_accounts_controller_create_or_update**
> BankAccountEntity bank_accounts_controller_create_or_update(create_or_update_bank_account_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_account_entity import BankAccountEntity
from python_core_api_sdk.models.create_or_update_bank_account_request_dto import CreateOrUpdateBankAccountRequestDto
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
    api_instance = python_core_api_sdk.BankAccountsApi(api_client)
    create_or_update_bank_account_request_dto = python_core_api_sdk.CreateOrUpdateBankAccountRequestDto() # CreateOrUpdateBankAccountRequestDto | 

    try:
        api_response = await api_instance.bank_accounts_controller_create_or_update(create_or_update_bank_account_request_dto)
        print("The response of BankAccountsApi->bank_accounts_controller_create_or_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->bank_accounts_controller_create_or_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_or_update_bank_account_request_dto** | [**CreateOrUpdateBankAccountRequestDto**](CreateOrUpdateBankAccountRequestDto.md)|  | 

### Return type

[**BankAccountEntity**](BankAccountEntity.md)

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

# **bank_accounts_controller_create_workspace_balance_report**
> BankAccountsBalanceReportEntity bank_accounts_controller_create_workspace_balance_report(workspace_id, enabled=enabled, types=types)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_accounts_balance_report_entity import BankAccountsBalanceReportEntity
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
    api_instance = python_core_api_sdk.BankAccountsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    enabled = True # bool |  (optional)
    types = 'types_example' # str |  (optional)

    try:
        api_response = await api_instance.bank_accounts_controller_create_workspace_balance_report(workspace_id, enabled=enabled, types=types)
        print("The response of BankAccountsApi->bank_accounts_controller_create_workspace_balance_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->bank_accounts_controller_create_workspace_balance_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **enabled** | **bool**|  | [optional] 
 **types** | **str**|  | [optional] 

### Return type

[**BankAccountsBalanceReportEntity**](BankAccountsBalanceReportEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_accounts_controller_disable**
> BankAccountEntity bank_accounts_controller_disable(bank_account_id)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_account_entity import BankAccountEntity
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
    api_instance = python_core_api_sdk.BankAccountsApi(api_client)
    bank_account_id = 'bank_account_id_example' # str | 

    try:
        api_response = await api_instance.bank_accounts_controller_disable(bank_account_id)
        print("The response of BankAccountsApi->bank_accounts_controller_disable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->bank_accounts_controller_disable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**|  | 

### Return type

[**BankAccountEntity**](BankAccountEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_accounts_controller_get_by_id**
> BankAccountEntity bank_accounts_controller_get_by_id(bank_account_id)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_account_entity import BankAccountEntity
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
    api_instance = python_core_api_sdk.BankAccountsApi(api_client)
    bank_account_id = 'bank_account_id_example' # str | 

    try:
        api_response = await api_instance.bank_accounts_controller_get_by_id(bank_account_id)
        print("The response of BankAccountsApi->bank_accounts_controller_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->bank_accounts_controller_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**|  | 

### Return type

[**BankAccountEntity**](BankAccountEntity.md)

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

# **bank_accounts_controller_list_by_bank_connection_id**
> List[BankAccountEntity] bank_accounts_controller_list_by_bank_connection_id(bank_connection_id, enabled=enabled, types=types)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_account_entity import BankAccountEntity
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
    api_instance = python_core_api_sdk.BankAccountsApi(api_client)
    bank_connection_id = 'bank_connection_id_example' # str | 
    enabled = True # bool |  (optional)
    types = 'types_example' # str |  (optional)

    try:
        api_response = await api_instance.bank_accounts_controller_list_by_bank_connection_id(bank_connection_id, enabled=enabled, types=types)
        print("The response of BankAccountsApi->bank_accounts_controller_list_by_bank_connection_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->bank_accounts_controller_list_by_bank_connection_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_connection_id** | **str**|  | 
 **enabled** | **bool**|  | [optional] 
 **types** | **str**|  | [optional] 

### Return type

[**List[BankAccountEntity]**](BankAccountEntity.md)

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

# **bank_accounts_controller_list_by_workspace_id**
> List[BankAccountEntity] bank_accounts_controller_list_by_workspace_id(workspace_id, enabled=enabled, types=types)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_account_entity import BankAccountEntity
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
    api_instance = python_core_api_sdk.BankAccountsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    enabled = True # bool |  (optional)
    types = 'types_example' # str |  (optional)

    try:
        api_response = await api_instance.bank_accounts_controller_list_by_workspace_id(workspace_id, enabled=enabled, types=types)
        print("The response of BankAccountsApi->bank_accounts_controller_list_by_workspace_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->bank_accounts_controller_list_by_workspace_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **enabled** | **bool**|  | [optional] 
 **types** | **str**|  | [optional] 

### Return type

[**List[BankAccountEntity]**](BankAccountEntity.md)

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

