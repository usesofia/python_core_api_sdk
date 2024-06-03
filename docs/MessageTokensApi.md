# python_core_api_sdk.MessageTokensApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**message_tokens_controller_create_or_update_message_token**](MessageTokensApi.md#message_tokens_controller_create_or_update_message_token) | **PUT** /workspaces/{workspaceId}/message-tokens | 
[**message_tokens_controller_get_workspace_message_tokens**](MessageTokensApi.md#message_tokens_controller_get_workspace_message_tokens) | **GET** /workspaces/{workspaceId}/message-tokens | 


# **message_tokens_controller_create_or_update_message_token**
> MessageTokenEntity message_tokens_controller_create_or_update_message_token(workspace_id, create_or_update_message_token_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.create_or_update_message_token_request_dto import CreateOrUpdateMessageTokenRequestDto
from python_core_api_sdk.models.message_token_entity import MessageTokenEntity
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
    api_instance = python_core_api_sdk.MessageTokensApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    create_or_update_message_token_request_dto = python_core_api_sdk.CreateOrUpdateMessageTokenRequestDto() # CreateOrUpdateMessageTokenRequestDto | 

    try:
        api_response = await api_instance.message_tokens_controller_create_or_update_message_token(workspace_id, create_or_update_message_token_request_dto)
        print("The response of MessageTokensApi->message_tokens_controller_create_or_update_message_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessageTokensApi->message_tokens_controller_create_or_update_message_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **create_or_update_message_token_request_dto** | [**CreateOrUpdateMessageTokenRequestDto**](CreateOrUpdateMessageTokenRequestDto.md)|  | 

### Return type

[**MessageTokenEntity**](MessageTokenEntity.md)

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

# **message_tokens_controller_get_workspace_message_tokens**
> List[MessageTokenEntity] message_tokens_controller_get_workspace_message_tokens(workspace_id)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.message_token_entity import MessageTokenEntity
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
    api_instance = python_core_api_sdk.MessageTokensApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        api_response = await api_instance.message_tokens_controller_get_workspace_message_tokens(workspace_id)
        print("The response of MessageTokensApi->message_tokens_controller_get_workspace_message_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessageTokensApi->message_tokens_controller_get_workspace_message_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[MessageTokenEntity]**](MessageTokenEntity.md)

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

