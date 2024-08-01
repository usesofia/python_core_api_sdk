# SyncBankAccountTransactionsPageBeginRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_item_id** | **str** |  | 
**page_number** | **int** |  | 

## Example

```python
from python_core_api_sdk.models.sync_bank_account_transactions_page_begin_request_dto import SyncBankAccountTransactionsPageBeginRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SyncBankAccountTransactionsPageBeginRequestDto from a JSON string
sync_bank_account_transactions_page_begin_request_dto_instance = SyncBankAccountTransactionsPageBeginRequestDto.from_json(json)
# print the JSON string representation of the object
print(SyncBankAccountTransactionsPageBeginRequestDto.to_json())

# convert the object into a dict
sync_bank_account_transactions_page_begin_request_dto_dict = sync_bank_account_transactions_page_begin_request_dto_instance.to_dict()
# create an instance of SyncBankAccountTransactionsPageBeginRequestDto from a dict
sync_bank_account_transactions_page_begin_request_dto_from_dict = SyncBankAccountTransactionsPageBeginRequestDto.from_dict(sync_bank_account_transactions_page_begin_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


