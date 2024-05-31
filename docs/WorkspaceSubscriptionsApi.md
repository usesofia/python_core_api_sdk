# openapi_client.WorkspaceSubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspace_subscriptions_controller_get**](WorkspaceSubscriptionsApi.md#workspace_subscriptions_controller_get) | **GET** /workspaces/{workspaceId}/subscription | 


# **workspace_subscriptions_controller_get**
> WorkspaceSubscriptionEntity workspace_subscriptions_controller_get(workspace_id)



### Example


```python
import openapi_client
from openapi_client.models.workspace_subscription_entity import WorkspaceSubscriptionEntity
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
    api_instance = openapi_client.WorkspaceSubscriptionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        api_response = api_instance.workspace_subscriptions_controller_get(workspace_id)
        print("The response of WorkspaceSubscriptionsApi->workspace_subscriptions_controller_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceSubscriptionsApi->workspace_subscriptions_controller_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**WorkspaceSubscriptionEntity**](WorkspaceSubscriptionEntity.md)

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

