# BankTransactionCreditCardMetadataEntity


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
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.bank_transaction_credit_card_metadata_entity import BankTransactionCreditCardMetadataEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionCreditCardMetadataEntity from a JSON string
bank_transaction_credit_card_metadata_entity_instance = BankTransactionCreditCardMetadataEntity.from_json(json)
# print the JSON string representation of the object
print(BankTransactionCreditCardMetadataEntity.to_json())

# convert the object into a dict
bank_transaction_credit_card_metadata_entity_dict = bank_transaction_credit_card_metadata_entity_instance.to_dict()
# create an instance of BankTransactionCreditCardMetadataEntity from a dict
bank_transaction_credit_card_metadata_entity_from_dict = BankTransactionCreditCardMetadataEntity.from_dict(bank_transaction_credit_card_metadata_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


