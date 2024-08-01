# SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  | 
**page_size** | **int** |  | 
**total_pages** | **int** |  | 
**total_results** | **int** |  | 
**transactions** | [**List[SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInner]**](SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInner.md) |  | 

## Example

```python
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page import SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage from a JSON string
sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_instance = SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage.from_json(json)
# print the JSON string representation of the object
print(SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage.to_json())

# convert the object into a dict
sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_dict = sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_instance.to_dict()
# create an instance of SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage from a dict
sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_from_dict = SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage.from_dict(sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


