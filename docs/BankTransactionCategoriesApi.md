# openapi_client.BankTransactionCategoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_transaction_categories_controller_get_bank_transaction_categories**](BankTransactionCategoriesApi.md#bank_transaction_categories_controller_get_bank_transaction_categories) | **GET** /workspaces/{workspaceId}/bank/transactions/categories | 


# **bank_transaction_categories_controller_get_bank_transaction_categories**
> List[BankTransactionCategoryEntity] bank_transaction_categories_controller_get_bank_transaction_categories(workspace_id, only_leafs=only_leafs, transaction_natures=transaction_natures, legal_natures=legal_natures)



### Example


```python
import openapi_client
from openapi_client.models.bank_transaction_category_entity import BankTransactionCategoryEntity
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
    api_instance = openapi_client.BankTransactionCategoriesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    only_leafs = True # bool |  (optional)
    transaction_natures = 'transaction_natures_example' # str |  (optional)
    legal_natures = 'legal_natures_example' # str |  (optional)

    try:
        api_response = api_instance.bank_transaction_categories_controller_get_bank_transaction_categories(workspace_id, only_leafs=only_leafs, transaction_natures=transaction_natures, legal_natures=legal_natures)
        print("The response of BankTransactionCategoriesApi->bank_transaction_categories_controller_get_bank_transaction_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionCategoriesApi->bank_transaction_categories_controller_get_bank_transaction_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **only_leafs** | **bool**|  | [optional] 
 **transaction_natures** | **str**|  | [optional] 
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

