# BankTransactionCategoryEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**nature** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**path** | [**List[BankTransactionCategoryPlainEntity]**](BankTransactionCategoryPlainEntity.md) |  | 
**children** | [**List[BankTransactionCategoryPlainEntity]**](BankTransactionCategoryPlainEntity.md) |  | 

## Example

```python
from openapi_client.models.bank_transaction_category_entity import BankTransactionCategoryEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionCategoryEntity from a JSON string
bank_transaction_category_entity_instance = BankTransactionCategoryEntity.from_json(json)
# print the JSON string representation of the object
print(BankTransactionCategoryEntity.to_json())

# convert the object into a dict
bank_transaction_category_entity_dict = bank_transaction_category_entity_instance.to_dict()
# create an instance of BankTransactionCategoryEntity from a dict
bank_transaction_category_entity_from_dict = BankTransactionCategoryEntity.from_dict(bank_transaction_category_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


