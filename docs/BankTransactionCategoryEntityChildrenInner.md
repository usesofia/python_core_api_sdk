# BankTransactionCategoryEntityChildrenInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**direction_nature** | **str** |  | 
**parent_id** | **str** |  | [optional] 

## Example

```python
from python_core_api_sdk.models.bank_transaction_category_entity_children_inner import BankTransactionCategoryEntityChildrenInner

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionCategoryEntityChildrenInner from a JSON string
bank_transaction_category_entity_children_inner_instance = BankTransactionCategoryEntityChildrenInner.from_json(json)
# print the JSON string representation of the object
print(BankTransactionCategoryEntityChildrenInner.to_json())

# convert the object into a dict
bank_transaction_category_entity_children_inner_dict = bank_transaction_category_entity_children_inner_instance.to_dict()
# create an instance of BankTransactionCategoryEntityChildrenInner from a dict
bank_transaction_category_entity_children_inner_from_dict = BankTransactionCategoryEntityChildrenInner.from_dict(bank_transaction_category_entity_children_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


