# BankTransactionTagEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.bank_transaction_tag_entity import BankTransactionTagEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionTagEntity from a JSON string
bank_transaction_tag_entity_instance = BankTransactionTagEntity.from_json(json)
# print the JSON string representation of the object
print(BankTransactionTagEntity.to_json())

# convert the object into a dict
bank_transaction_tag_entity_dict = bank_transaction_tag_entity_instance.to_dict()
# create an instance of BankTransactionTagEntity from a dict
bank_transaction_tag_entity_from_dict = BankTransactionTagEntity.from_dict(bank_transaction_tag_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


