# openapi_client.PluggyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pluggy_controller_create**](PluggyApi.md#pluggy_controller_create) | **POST** /pluggy/connect-token | 
[**pluggy_controller_webhook**](PluggyApi.md#pluggy_controller_webhook) | **POST** /pluggy/webhook | 


# **pluggy_controller_create**
> PluggyConnectTokenEntity pluggy_controller_create(create_pluggy_connect_token_request_dto)



### Example


```python
import openapi_client
from openapi_client.models.create_pluggy_connect_token_request_dto import CreatePluggyConnectTokenRequestDto
from openapi_client.models.pluggy_connect_token_entity import PluggyConnectTokenEntity
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluggyApi(api_client)
    create_pluggy_connect_token_request_dto = openapi_client.CreatePluggyConnectTokenRequestDto() # CreatePluggyConnectTokenRequestDto | 

    try:
        api_response = api_instance.pluggy_controller_create(create_pluggy_connect_token_request_dto)
        print("The response of PluggyApi->pluggy_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluggyApi->pluggy_controller_create: %s\n" % e)
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
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluggyApi(api_client)

    try:
        api_instance.pluggy_controller_webhook()
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
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

