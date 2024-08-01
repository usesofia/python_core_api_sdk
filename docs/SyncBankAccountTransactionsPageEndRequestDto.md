# SyncBankAccountTransactionsPageEndRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_item_id** | **str** |  | 
**page_number** | **int** |  | 
**bank_provider_transactions_page** | [**SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage**](SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage.md) |  | 
**legal_nature_assign_requests** | [**List[SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner]**](SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner.md) |  | 
**category_assign_requests** | [**List[SyncBankAccountTransactionsPageEndRequestDtoCategoryAssignRequestsInner]**](SyncBankAccountTransactionsPageEndRequestDtoCategoryAssignRequestsInner.md) |  | 

## Example

```python
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto import SyncBankAccountTransactionsPageEndRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SyncBankAccountTransactionsPageEndRequestDto from a JSON string
sync_bank_account_transactions_page_end_request_dto_instance = SyncBankAccountTransactionsPageEndRequestDto.from_json(json)
# print the JSON string representation of the object
print(SyncBankAccountTransactionsPageEndRequestDto.to_json())

# convert the object into a dict
sync_bank_account_transactions_page_end_request_dto_dict = sync_bank_account_transactions_page_end_request_dto_instance.to_dict()
# create an instance of SyncBankAccountTransactionsPageEndRequestDto from a dict
sync_bank_account_transactions_page_end_request_dto_from_dict = SyncBankAccountTransactionsPageEndRequestDto.from_dict(sync_bank_account_transactions_page_end_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


