# SyncBankAccountTransactionsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**provider** | **str** |  | 
**provider_account_id** | **str** |  | 
**provider_item_id** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.sync_bank_account_transactions_request_dto import SyncBankAccountTransactionsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SyncBankAccountTransactionsRequestDto from a JSON string
sync_bank_account_transactions_request_dto_instance = SyncBankAccountTransactionsRequestDto.from_json(json)
# print the JSON string representation of the object
print(SyncBankAccountTransactionsRequestDto.to_json())

# convert the object into a dict
sync_bank_account_transactions_request_dto_dict = sync_bank_account_transactions_request_dto_instance.to_dict()
# create an instance of SyncBankAccountTransactionsRequestDto from a dict
sync_bank_account_transactions_request_dto_from_dict = SyncBankAccountTransactionsRequestDto.from_dict(sync_bank_account_transactions_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


