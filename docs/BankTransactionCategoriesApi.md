# python_core_api_sdk.BankTransactionCategoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_transaction_categories_controller_list**](BankTransactionCategoriesApi.md#bank_transaction_categories_controller_list) | **GET** /bank/workspaces/{workspaceId}/transaction-categories | 


# **bank_transaction_categories_controller_list**
> List[BankTransactionCategoryEntity] bank_transaction_categories_controller_list(workspace_id, only_leafs=only_leafs, direction_natures=direction_natures, legal_natures=legal_natures)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_transaction_category_entity import BankTransactionCategoryEntity
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
    api_instance = python_core_api_sdk.BankTransactionCategoriesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    only_leafs = True # bool |  (optional)
    direction_natures = 'direction_natures_example' # str |  (optional)
    legal_natures = 'legal_natures_example' # str |  (optional)

    try:
        api_response = await api_instance.bank_transaction_categories_controller_list(workspace_id, only_leafs=only_leafs, direction_natures=direction_natures, legal_natures=legal_natures)
        print("The response of BankTransactionCategoriesApi->bank_transaction_categories_controller_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionCategoriesApi->bank_transaction_categories_controller_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **only_leafs** | **bool**|  | [optional] 
 **direction_natures** | **str**|  | [optional] 
 **legal_natures** | **str**|  | [optional] 

### Return type

[**List[BankTransactionCategoryEntity]**](BankTransactionCategoryEntity.md)

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

