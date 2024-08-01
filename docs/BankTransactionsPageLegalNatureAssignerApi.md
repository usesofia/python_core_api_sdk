# python_core_api_sdk.BankTransactionsPageLegalNatureAssignerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_transactions_page_legal_nature_assigner_controller_assign**](BankTransactionsPageLegalNatureAssignerApi.md#bank_transactions_page_legal_nature_assigner_controller_assign) | **POST** /bank/transactions/page/legal-nature/assign | 


# **bank_transactions_page_legal_nature_assigner_controller_assign**
> bank_transactions_page_legal_nature_assigner_controller_assign(assign_legal_nature_for_bank_transactions_page_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.assign_legal_nature_for_bank_transactions_page_request_dto import AssignLegalNatureForBankTransactionsPageRequestDto
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
    api_instance = python_core_api_sdk.BankTransactionsPageLegalNatureAssignerApi(api_client)
    assign_legal_nature_for_bank_transactions_page_request_dto = python_core_api_sdk.AssignLegalNatureForBankTransactionsPageRequestDto() # AssignLegalNatureForBankTransactionsPageRequestDto | 

    try:
        await api_instance.bank_transactions_page_legal_nature_assigner_controller_assign(assign_legal_nature_for_bank_transactions_page_request_dto)
    except Exception as e:
        print("Exception when calling BankTransactionsPageLegalNatureAssignerApi->bank_transactions_page_legal_nature_assigner_controller_assign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_legal_nature_for_bank_transactions_page_request_dto** | [**AssignLegalNatureForBankTransactionsPageRequestDto**](AssignLegalNatureForBankTransactionsPageRequestDto.md)|  | 

### Return type

void (empty response body)

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

