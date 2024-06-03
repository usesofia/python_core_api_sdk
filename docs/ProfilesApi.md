# python_core_api_sdk.ProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profiles_controller_create**](ProfilesApi.md#profiles_controller_create) | **POST** /profiles | 
[**profiles_controller_get_my**](ProfilesApi.md#profiles_controller_get_my) | **GET** /profiles/me | 
[**profiles_controller_parcial_update**](ProfilesApi.md#profiles_controller_parcial_update) | **PATCH** /profiles/me | 


# **profiles_controller_create**
> ProfileEntity profiles_controller_create(create_profile_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.create_profile_request_dto import CreateProfileRequestDto
from python_core_api_sdk.models.profile_entity import ProfileEntity
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
    api_instance = python_core_api_sdk.ProfilesApi(api_client)
    create_profile_request_dto = python_core_api_sdk.CreateProfileRequestDto() # CreateProfileRequestDto | 

    try:
        api_response = await api_instance.profiles_controller_create(create_profile_request_dto)
        print("The response of ProfilesApi->profiles_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->profiles_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_profile_request_dto** | [**CreateProfileRequestDto**](CreateProfileRequestDto.md)|  | 

### Return type

[**ProfileEntity**](ProfileEntity.md)

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

# **profiles_controller_get_my**
> ProfileEntity profiles_controller_get_my()



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.profile_entity import ProfileEntity
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
    api_instance = python_core_api_sdk.ProfilesApi(api_client)

    try:
        api_response = await api_instance.profiles_controller_get_my()
        print("The response of ProfilesApi->profiles_controller_get_my:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->profiles_controller_get_my: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProfileEntity**](ProfileEntity.md)

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

# **profiles_controller_parcial_update**
> ProfileEntity profiles_controller_parcial_update(parcial_update_profile_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.parcial_update_profile_request_dto import ParcialUpdateProfileRequestDto
from python_core_api_sdk.models.profile_entity import ProfileEntity
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
    api_instance = python_core_api_sdk.ProfilesApi(api_client)
    parcial_update_profile_request_dto = python_core_api_sdk.ParcialUpdateProfileRequestDto() # ParcialUpdateProfileRequestDto | 

    try:
        api_response = await api_instance.profiles_controller_parcial_update(parcial_update_profile_request_dto)
        print("The response of ProfilesApi->profiles_controller_parcial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->profiles_controller_parcial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcial_update_profile_request_dto** | [**ParcialUpdateProfileRequestDto**](ParcialUpdateProfileRequestDto.md)|  | 

### Return type

[**ProfileEntity**](ProfileEntity.md)

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

