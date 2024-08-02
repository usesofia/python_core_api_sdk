# BankTransactionEntityPaymentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transaction_id** | **str** |  | 
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
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.bank_transaction_entity_payment_data import BankTransactionEntityPaymentData

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionEntityPaymentData from a JSON string
bank_transaction_entity_payment_data_instance = BankTransactionEntityPaymentData.from_json(json)
# print the JSON string representation of the object
print(BankTransactionEntityPaymentData.to_json())

# convert the object into a dict
bank_transaction_entity_payment_data_dict = bank_transaction_entity_payment_data_instance.to_dict()
# create an instance of BankTransactionEntityPaymentData from a dict
bank_transaction_entity_payment_data_from_dict = BankTransactionEntityPaymentData.from_dict(bank_transaction_entity_payment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


