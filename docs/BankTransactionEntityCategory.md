# BankTransactionEntityCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**direction_nature** | **str** |  | 
**parent_id** | **str** |  | [optional] 

## Example

```python
from python_core_api_sdk.models.bank_transaction_entity_category import BankTransactionEntityCategory

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionEntityCategory from a JSON string
bank_transaction_entity_category_instance = BankTransactionEntityCategory.from_json(json)
# print the JSON string representation of the object
print(BankTransactionEntityCategory.to_json())

# convert the object into a dict
bank_transaction_entity_category_dict = bank_transaction_entity_category_instance.to_dict()
# create an instance of BankTransactionEntityCategory from a dict
bank_transaction_entity_category_from_dict = BankTransactionEntityCategory.from_dict(bank_transaction_entity_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


