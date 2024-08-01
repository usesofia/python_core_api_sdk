# AssignCategoryForBankTransactionsPageRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_item_id** | **str** |  | 
**page_number** | **int** |  | 
**bank_provider_transactions_page** | [**SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage**](SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage.md) |  | 
**legal_nature_assign_requests** | [**List[SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner]**](SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner.md) |  | 

## Example

```python
from python_core_api_sdk.models.assign_category_for_bank_transactions_page_request_dto import AssignCategoryForBankTransactionsPageRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssignCategoryForBankTransactionsPageRequestDto from a JSON string
assign_category_for_bank_transactions_page_request_dto_instance = AssignCategoryForBankTransactionsPageRequestDto.from_json(json)
# print the JSON string representation of the object
print(AssignCategoryForBankTransactionsPageRequestDto.to_json())

# convert the object into a dict
assign_category_for_bank_transactions_page_request_dto_dict = assign_category_for_bank_transactions_page_request_dto_instance.to_dict()
# create an instance of AssignCategoryForBankTransactionsPageRequestDto from a dict
assign_category_for_bank_transactions_page_request_dto_from_dict = AssignCategoryForBankTransactionsPageRequestDto.from_dict(assign_category_for_bank_transactions_page_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


