# python_core_api_sdk.BankConnectionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_connections_controller_activate_bank_connection**](BankConnectionsApi.md#bank_connections_controller_activate_bank_connection) | **POST** /bank/connections/{bankConnectionId}/activate | 
[**bank_connections_controller_create_or_update_bank_connection**](BankConnectionsApi.md#bank_connections_controller_create_or_update_bank_connection) | **PUT** /workspaces/{workspaceId}/bank/connections | 
[**bank_connections_controller_disable_bank_connection**](BankConnectionsApi.md#bank_connections_controller_disable_bank_connection) | **POST** /bank/connections/{bankConnectionId}/disable | 
[**bank_connections_controller_fetch_user_bank_connections**](BankConnectionsApi.md#bank_connections_controller_fetch_user_bank_connections) | **GET** /workspaces/{workspaceId}/bank/connections | 
[**bank_connections_controller_get_bank_connection_details**](BankConnectionsApi.md#bank_connections_controller_get_bank_connection_details) | **GET** /bank/connections/{bankConnectionId} | 


# **bank_connections_controller_activate_bank_connection**
> BankConnectionEntity bank_connections_controller_activate_bank_connection(bank_connection_id)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_connection_entity import BankConnectionEntity
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
    api_instance = python_core_api_sdk.BankConnectionsApi(api_client)
    bank_connection_id = 'bank_connection_id_example' # str | 

    try:
        api_response = await api_instance.bank_connections_controller_activate_bank_connection(bank_connection_id)
        print("The response of BankConnectionsApi->bank_connections_controller_activate_bank_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankConnectionsApi->bank_connections_controller_activate_bank_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_connection_id** | **str**|  | 

### Return type

[**BankConnectionEntity**](BankConnectionEntity.md)

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

# **bank_connections_controller_create_or_update_bank_connection**
> BankConnectionEntity bank_connections_controller_create_or_update_bank_connection(workspace_id, create_or_update_bank_connection_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_connection_entity import BankConnectionEntity
from python_core_api_sdk.models.create_or_update_bank_connection_request_dto import CreateOrUpdateBankConnectionRequestDto
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
    api_instance = python_core_api_sdk.BankConnectionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    create_or_update_bank_connection_request_dto = python_core_api_sdk.CreateOrUpdateBankConnectionRequestDto() # CreateOrUpdateBankConnectionRequestDto | 

    try:
        api_response = await api_instance.bank_connections_controller_create_or_update_bank_connection(workspace_id, create_or_update_bank_connection_request_dto)
        print("The response of BankConnectionsApi->bank_connections_controller_create_or_update_bank_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankConnectionsApi->bank_connections_controller_create_or_update_bank_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **create_or_update_bank_connection_request_dto** | [**CreateOrUpdateBankConnectionRequestDto**](CreateOrUpdateBankConnectionRequestDto.md)|  | 

### Return type

[**BankConnectionEntity**](BankConnectionEntity.md)

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

# **bank_connections_controller_disable_bank_connection**
> BankConnectionEntity bank_connections_controller_disable_bank_connection(bank_connection_id)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_connection_entity import BankConnectionEntity
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
    api_instance = python_core_api_sdk.BankConnectionsApi(api_client)
    bank_connection_id = 'bank_connection_id_example' # str | 

    try:
        api_response = await api_instance.bank_connections_controller_disable_bank_connection(bank_connection_id)
        print("The response of BankConnectionsApi->bank_connections_controller_disable_bank_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankConnectionsApi->bank_connections_controller_disable_bank_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_connection_id** | **str**|  | 

### Return type

[**BankConnectionEntity**](BankConnectionEntity.md)

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

# **bank_connections_controller_fetch_user_bank_connections**
> List[BankConnectionWithAccountsEntity] bank_connections_controller_fetch_user_bank_connections(workspace_id, enabled=enabled)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_connection_with_accounts_entity import BankConnectionWithAccountsEntity
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
    api_instance = python_core_api_sdk.BankConnectionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    enabled = True # bool |  (optional)

    try:
        api_response = await api_instance.bank_connections_controller_fetch_user_bank_connections(workspace_id, enabled=enabled)
        print("The response of BankConnectionsApi->bank_connections_controller_fetch_user_bank_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankConnectionsApi->bank_connections_controller_fetch_user_bank_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **enabled** | **bool**|  | [optional] 

### Return type

[**List[BankConnectionWithAccountsEntity]**](BankConnectionWithAccountsEntity.md)

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

# **bank_connections_controller_get_bank_connection_details**
> BankConnectionWithAccountsEntity bank_connections_controller_get_bank_connection_details(bank_connection_id)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_connection_with_accounts_entity import BankConnectionWithAccountsEntity
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
    api_instance = python_core_api_sdk.BankConnectionsApi(api_client)
    bank_connection_id = 'bank_connection_id_example' # str | 

    try:
        api_response = await api_instance.bank_connections_controller_get_bank_connection_details(bank_connection_id)
        print("The response of BankConnectionsApi->bank_connections_controller_get_bank_connection_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankConnectionsApi->bank_connections_controller_get_bank_connection_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_connection_id** | **str**|  | 

### Return type

[**BankConnectionWithAccountsEntity**](BankConnectionWithAccountsEntity.md)

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

