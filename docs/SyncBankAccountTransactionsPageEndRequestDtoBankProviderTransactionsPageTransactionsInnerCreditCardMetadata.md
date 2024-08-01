# SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerCreditCardMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installment_number** | **float** |  | [optional] 
**total_installments** | **float** |  | [optional] 
**total_amount** | **float** |  | [optional] 
**payee_mcc** | **float** |  | [optional] 
**card_number** | **str** |  | [optional] 
**bill_id** | **str** |  | [optional] 

## Example

```python
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_credit_card_metadata import SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerCreditCardMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerCreditCardMetadata from a JSON string
sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_credit_card_metadata_instance = SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerCreditCardMetadata.from_json(json)
# print the JSON string representation of the object
print(SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerCreditCardMetadata.to_json())

# convert the object into a dict
sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_credit_card_metadata_dict = sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_credit_card_metadata_instance.to_dict()
# create an instance of SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerCreditCardMetadata from a dict
sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_credit_card_metadata_from_dict = SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerCreditCardMetadata.from_dict(sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_credit_card_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


