# openapi_client.WorkspaceJoinRequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspace_join_requests_controller_create_new_pending_or_return_current**](WorkspaceJoinRequestsApi.md#workspace_join_requests_controller_create_new_pending_or_return_current) | **POST** /workspaces/{workspaceId}/join-requests | 


# **workspace_join_requests_controller_create_new_pending_or_return_current**
> WorkspaceJoinRequestEntity workspace_join_requests_controller_create_new_pending_or_return_current(workspace_id)



### Example


```python
import openapi_client
from openapi_client.models.workspace_join_request_entity import WorkspaceJoinRequestEntity
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
    api_instance = openapi_client.WorkspaceJoinRequestsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        api_response = api_instance.workspace_join_requests_controller_create_new_pending_or_return_current(workspace_id)
        print("The response of WorkspaceJoinRequestsApi->workspace_join_requests_controller_create_new_pending_or_return_current:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceJoinRequestsApi->workspace_join_requests_controller_create_new_pending_or_return_current: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**WorkspaceJoinRequestEntity**](WorkspaceJoinRequestEntity.md)

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

