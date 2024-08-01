# SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer_name** | **str** |  | [optional] 
**payer_branch_number** | **str** |  | [optional] 
**payer_account_number** | **str** |  | [optional] 
**payer_routing_number** | **str** |  | [optional] 
**payer_routing_number_ispb** | **str** |  | [optional] 
**payer_document_number_type** | **str** |  | [optional] 
**payer_document_number_value** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**receiver_name** | **str** |  | [optional] 
**receiver_branch_number** | **str** |  | [optional] 
**receiver_account_number** | **str** |  | [optional] 
**receiver_routing_number** | **str** |  | [optional] 
**receiver_routing_number_ispb** | **str** |  | [optional] 
**receiver_document_number_type** | **str** |  | [optional] 
**receiver_document_number_value** | **str** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**receiver_reference_id** | **str** |  | [optional] 

## Example

```python
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_payment_data import SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData

# TODO update the JSON string below
json = "{}"
# create an instance of SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData from a JSON string
sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_payment_data_instance = SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData.from_json(json)
# print the JSON string representation of the object
print(SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData.to_json())

# convert the object into a dict
sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_payment_data_dict = sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_payment_data_instance.to_dict()
# create an instance of SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData from a dict
sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_payment_data_from_dict = SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData.from_dict(sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_payment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


