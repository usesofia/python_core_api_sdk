# BankTransactionEntityCreditCardMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transaction_id** | **str** |  | 
**installment_number** | **float** |  | [optional] 
**total_installments** | **float** |  | [optional] 
**total_amount** | **float** |  | [optional] 
**payee_mcc** | **float** |  | [optional] 
**card_number** | **str** |  | [optional] 
**bill_id** | **str** |  | [optional] 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 

## Example

```python
from python_core_api_sdk.models.bank_transaction_entity_credit_card_metadata import BankTransactionEntityCreditCardMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionEntityCreditCardMetadata from a JSON string
bank_transaction_entity_credit_card_metadata_instance = BankTransactionEntityCreditCardMetadata.from_json(json)
# print the JSON string representation of the object
print(BankTransactionEntityCreditCardMetadata.to_json())

# convert the object into a dict
bank_transaction_entity_credit_card_metadata_dict = bank_transaction_entity_credit_card_metadata_instance.to_dict()
# create an instance of BankTransactionEntityCreditCardMetadata from a dict
bank_transaction_entity_credit_card_metadata_from_dict = BankTransactionEntityCreditCardMetadata.from_dict(bank_transaction_entity_credit_card_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


