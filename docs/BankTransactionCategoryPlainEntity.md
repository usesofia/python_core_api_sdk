# BankTransactionCategoryPlainEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**nature** | **str** |  | 
**parent_id** | **str** |  | [optional] 

## Example

```python
from python_core_api_sdk.models.bank_transaction_category_plain_entity import BankTransactionCategoryPlainEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionCategoryPlainEntity from a JSON string
bank_transaction_category_plain_entity_instance = BankTransactionCategoryPlainEntity.from_json(json)
# print the JSON string representation of the object
print(BankTransactionCategoryPlainEntity.to_json())

# convert the object into a dict
bank_transaction_category_plain_entity_dict = bank_transaction_category_plain_entity_instance.to_dict()
# create an instance of BankTransactionCategoryPlainEntity from a dict
bank_transaction_category_plain_entity_from_dict = BankTransactionCategoryPlainEntity.from_dict(bank_transaction_category_plain_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


