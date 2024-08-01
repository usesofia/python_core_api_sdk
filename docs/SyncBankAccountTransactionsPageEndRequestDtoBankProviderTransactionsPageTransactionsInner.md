# SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**description** | **str** |  | 
**posted_date** | **object** |  | 
**amount** | **int** |  | 
**direction_nature** | **str** |  | 
**status** | **str** |  | 
**category_id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**payment_data** | [**SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData**](SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData.md) |  | [optional] 
**credit_card_metadata** | [**SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerCreditCardMetadata**](SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerCreditCardMetadata.md) |  | [optional] 

## Example

```python
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner import SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInner from a JSON string
sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_instance = SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInner.from_json(json)
# print the JSON string representation of the object
print(SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInner.to_json())

# convert the object into a dict
sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_dict = sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_instance.to_dict()
# create an instance of SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInner from a dict
sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_from_dict = SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInner.from_dict(sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


