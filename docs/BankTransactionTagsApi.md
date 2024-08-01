# python_core_api_sdk.BankTransactionTagsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_transaction_tags_controller_create**](BankTransactionTagsApi.md#bank_transaction_tags_controller_create) | **POST** /bank/workspaces/{workspaceId}/transaction-tags | 
[**bank_transaction_tags_controller_list**](BankTransactionTagsApi.md#bank_transaction_tags_controller_list) | **GET** /bank/workspaces/{workspaceId}/transaction-tags | 


# **bank_transaction_tags_controller_create**
> BankTransactionTagEntity bank_transaction_tags_controller_create(workspace_id, create_bank_transaction_tag_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_transaction_tag_entity import BankTransactionTagEntity
from python_core_api_sdk.models.create_bank_transaction_tag_request_dto import CreateBankTransactionTagRequestDto
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
    api_instance = python_core_api_sdk.BankTransactionTagsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    create_bank_transaction_tag_request_dto = python_core_api_sdk.CreateBankTransactionTagRequestDto() # CreateBankTransactionTagRequestDto | 

    try:
        api_response = await api_instance.bank_transaction_tags_controller_create(workspace_id, create_bank_transaction_tag_request_dto)
        print("The response of BankTransactionTagsApi->bank_transaction_tags_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionTagsApi->bank_transaction_tags_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **create_bank_transaction_tag_request_dto** | [**CreateBankTransactionTagRequestDto**](CreateBankTransactionTagRequestDto.md)|  | 

### Return type

[**BankTransactionTagEntity**](BankTransactionTagEntity.md)

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

# **bank_transaction_tags_controller_list**
> List[BankTransactionTagEntity] bank_transaction_tags_controller_list(workspace_id)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.bank_transaction_tag_entity import BankTransactionTagEntity
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
    api_instance = python_core_api_sdk.BankTransactionTagsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        api_response = await api_instance.bank_transaction_tags_controller_list(workspace_id)
        print("The response of BankTransactionTagsApi->bank_transaction_tags_controller_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionTagsApi->bank_transaction_tags_controller_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[BankTransactionTagEntity]**](BankTransactionTagEntity.md)

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

