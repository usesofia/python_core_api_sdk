# python_core_api_sdk.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_controller_get**](UsersApi.md#users_controller_get) | **GET** /users/users/{userId} | 


# **users_controller_get**
> UserWithProfileEntity users_controller_get(user_id)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.user_with_profile_entity import UserWithProfileEntity
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
    api_instance = python_core_api_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        api_response = await api_instance.users_controller_get(user_id)
        print("The response of UsersApi->users_controller_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_controller_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserWithProfileEntity**](UserWithProfileEntity.md)

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

