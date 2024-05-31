# python_core_api_sdk.SubscriptionProductsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_products_controller_list**](SubscriptionProductsApi.md#subscription_products_controller_list) | **GET** /workspaces/{workspaceId}/subscription-products | 


# **subscription_products_controller_list**
> List[SubscriptionProductEntity] subscription_products_controller_list(workspace_id)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.subscription_product_entity import SubscriptionProductEntity
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.SubscriptionProductsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        api_response = api_instance.subscription_products_controller_list(workspace_id)
        print("The response of SubscriptionProductsApi->subscription_products_controller_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionProductsApi->subscription_products_controller_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[SubscriptionProductEntity]**](SubscriptionProductEntity.md)

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

