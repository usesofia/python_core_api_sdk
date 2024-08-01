# python_core_api_sdk.WorkspacesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspaces_controller_create**](WorkspacesApi.md#workspaces_controller_create) | **POST** /iam/workspaces | 
[**workspaces_controller_get_by_id**](WorkspacesApi.md#workspaces_controller_get_by_id) | **GET** /iam/workspaces/{workspaceId} | 
[**workspaces_controller_list_my**](WorkspacesApi.md#workspaces_controller_list_my) | **GET** /iam/workspaces/my | 
[**workspaces_controller_partial_update**](WorkspacesApi.md#workspaces_controller_partial_update) | **PATCH** /iam/workspaces/{workspaceId} | 


# **workspaces_controller_create**
> WorkspaceEntity workspaces_controller_create(create_workspace_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.create_workspace_request_dto import CreateWorkspaceRequestDto
from python_core_api_sdk.models.workspace_entity import WorkspaceEntity
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
    api_instance = python_core_api_sdk.WorkspacesApi(api_client)
    create_workspace_request_dto = python_core_api_sdk.CreateWorkspaceRequestDto() # CreateWorkspaceRequestDto | 

    try:
        api_response = await api_instance.workspaces_controller_create(create_workspace_request_dto)
        print("The response of WorkspacesApi->workspaces_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->workspaces_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workspace_request_dto** | [**CreateWorkspaceRequestDto**](CreateWorkspaceRequestDto.md)|  | 

### Return type

[**WorkspaceEntity**](WorkspaceEntity.md)

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

# **workspaces_controller_get_by_id**
> WorkspaceEntity workspaces_controller_get_by_id(workspace_id)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.workspace_entity import WorkspaceEntity
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
    api_instance = python_core_api_sdk.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        api_response = await api_instance.workspaces_controller_get_by_id(workspace_id)
        print("The response of WorkspacesApi->workspaces_controller_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->workspaces_controller_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**WorkspaceEntity**](WorkspaceEntity.md)

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

# **workspaces_controller_list_my**
> List[UserRelatedWorkspaceEntity] workspaces_controller_list_my()



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.user_related_workspace_entity import UserRelatedWorkspaceEntity
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
    api_instance = python_core_api_sdk.WorkspacesApi(api_client)

    try:
        api_response = await api_instance.workspaces_controller_list_my()
        print("The response of WorkspacesApi->workspaces_controller_list_my:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->workspaces_controller_list_my: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserRelatedWorkspaceEntity]**](UserRelatedWorkspaceEntity.md)

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

# **workspaces_controller_partial_update**
> WorkspaceEntity workspaces_controller_partial_update(workspace_id, partial_update_workspace_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.partial_update_workspace_request_dto import PartialUpdateWorkspaceRequestDto
from python_core_api_sdk.models.workspace_entity import WorkspaceEntity
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
    api_instance = python_core_api_sdk.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    partial_update_workspace_request_dto = python_core_api_sdk.PartialUpdateWorkspaceRequestDto() # PartialUpdateWorkspaceRequestDto | 

    try:
        api_response = await api_instance.workspaces_controller_partial_update(workspace_id, partial_update_workspace_request_dto)
        print("The response of WorkspacesApi->workspaces_controller_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->workspaces_controller_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **partial_update_workspace_request_dto** | [**PartialUpdateWorkspaceRequestDto**](PartialUpdateWorkspaceRequestDto.md)|  | 

### Return type

[**WorkspaceEntity**](WorkspaceEntity.md)

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

