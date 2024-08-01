# python_core_api_sdk.PluggyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pluggy_controller_create_connect_token**](PluggyApi.md#pluggy_controller_create_connect_token) | **POST** /pluggy/connect-tokens | 
[**pluggy_controller_webhook**](PluggyApi.md#pluggy_controller_webhook) | **POST** /pluggy/webhook | 


# **pluggy_controller_create_connect_token**
> PluggyConnectTokenEntity pluggy_controller_create_connect_token(create_pluggy_connect_token_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.create_pluggy_connect_token_request_dto import CreatePluggyConnectTokenRequestDto
from python_core_api_sdk.models.pluggy_connect_token_entity import PluggyConnectTokenEntity
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
    api_instance = python_core_api_sdk.PluggyApi(api_client)
    create_pluggy_connect_token_request_dto = python_core_api_sdk.CreatePluggyConnectTokenRequestDto() # CreatePluggyConnectTokenRequestDto | 

    try:
        api_response = await api_instance.pluggy_controller_create_connect_token(create_pluggy_connect_token_request_dto)
        print("The response of PluggyApi->pluggy_controller_create_connect_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluggyApi->pluggy_controller_create_connect_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_pluggy_connect_token_request_dto** | [**CreatePluggyConnectTokenRequestDto**](CreatePluggyConnectTokenRequestDto.md)|  | 

### Return type

[**PluggyConnectTokenEntity**](PluggyConnectTokenEntity.md)

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

# **pluggy_controller_webhook**
> pluggy_controller_webhook()



### Example


```python
import python_core_api_sdk
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
    api_instance = python_core_api_sdk.PluggyApi(api_client)

    try:
        await api_instance.pluggy_controller_webhook()
    except Exception as e:
        print("Exception when calling PluggyApi->pluggy_controller_webhook: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

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

