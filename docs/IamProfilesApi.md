# python_core_api_sdk.IamProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profiles_controller_get_my**](IamProfilesApi.md#profiles_controller_get_my) | **GET** /iam/profiles/me | 


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
    api_instance = python_core_api_sdk.IamProfilesApi(api_client)

    try:
        api_response = await api_instance.profiles_controller_get_my()
        print("The response of IamProfilesApi->profiles_controller_get_my:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamProfilesApi->profiles_controller_get_my: %s\n" % e)
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

