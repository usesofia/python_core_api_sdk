# CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData


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
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto_items_inner_payment_data import CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData from a JSON string
create_or_update_bank_transactions_in_bulk_request_dto_items_inner_payment_data_instance = CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData.to_json())

# convert the object into a dict
create_or_update_bank_transactions_in_bulk_request_dto_items_inner_payment_data_dict = create_or_update_bank_transactions_in_bulk_request_dto_items_inner_payment_data_instance.to_dict()
# create an instance of CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData from a dict
create_or_update_bank_transactions_in_bulk_request_dto_items_inner_payment_data_from_dict = CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData.from_dict(create_or_update_bank_transactions_in_bulk_request_dto_items_inner_payment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


