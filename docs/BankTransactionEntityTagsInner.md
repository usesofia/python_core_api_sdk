# BankTransactionEntityTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.bank_transaction_entity_tags_inner import BankTransactionEntityTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionEntityTagsInner from a JSON string
bank_transaction_entity_tags_inner_instance = BankTransactionEntityTagsInner.from_json(json)
# print the JSON string representation of the object
print(BankTransactionEntityTagsInner.to_json())

# convert the object into a dict
bank_transaction_entity_tags_inner_dict = bank_transaction_entity_tags_inner_instance.to_dict()
# create an instance of BankTransactionEntityTagsInner from a dict
bank_transaction_entity_tags_inner_from_dict = BankTransactionEntityTagsInner.from_dict(bank_transaction_entity_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


