# python_core_api_sdk.WorkspacesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspaces_controller_create**](WorkspacesApi.md#workspaces_controller_create) | **POST** /workspaces | 
[**workspaces_controller_fetch_user_related_workspaces**](WorkspacesApi.md#workspaces_controller_fetch_user_related_workspaces) | **GET** /workspaces/related-to-me | 
[**workspaces_controller_get**](WorkspacesApi.md#workspaces_controller_get) | **GET** /workspaces/{workspaceId} | 
[**workspaces_controller_parcial_update**](WorkspacesApi.md#workspaces_controller_parcial_update) | **PATCH** /workspaces/{workspaceId} | 


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

# **workspaces_controller_fetch_user_related_workspaces**
> List[UserRelatedWorkspaceEntity] workspaces_controller_fetch_user_related_workspaces()



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
        api_response = await api_instance.workspaces_controller_fetch_user_related_workspaces()
        print("The response of WorkspacesApi->workspaces_controller_fetch_user_related_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->workspaces_controller_fetch_user_related_workspaces: %s\n" % e)
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

# **workspaces_controller_get**
> WorkspaceEntity workspaces_controller_get(workspace_id)



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
        api_response = await api_instance.workspaces_controller_get(workspace_id)
        print("The response of WorkspacesApi->workspaces_controller_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->workspaces_controller_get: %s\n" % e)
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

# **workspaces_controller_parcial_update**
> WorkspaceEntity workspaces_controller_parcial_update(workspace_id, parcial_update_workspace_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.parcial_update_workspace_request_dto import ParcialUpdateWorkspaceRequestDto
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
    parcial_update_workspace_request_dto = python_core_api_sdk.ParcialUpdateWorkspaceRequestDto() # ParcialUpdateWorkspaceRequestDto | 

    try:
        api_response = await api_instance.workspaces_controller_parcial_update(workspace_id, parcial_update_workspace_request_dto)
        print("The response of WorkspacesApi->workspaces_controller_parcial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->workspaces_controller_parcial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **parcial_update_workspace_request_dto** | [**ParcialUpdateWorkspaceRequestDto**](ParcialUpdateWorkspaceRequestDto.md)|  | 

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

