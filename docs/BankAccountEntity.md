# BankAccountEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**bank_connection_id** | **str** |  | 
**provider** | **str** |  | 
**provider_account_id** | **str** |  | 
**type** | **str** |  | 
**enabled** | **bool** |  | 
**number** | **str** |  | 
**balance** | **int** |  | 
**currency_code** | **str** |  | 
**name** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 

## Example

```python
from python_core_api_sdk.models.bank_account_entity import BankAccountEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountEntity from a JSON string
bank_account_entity_instance = BankAccountEntity.from_json(json)
# print the JSON string representation of the object
print(BankAccountEntity.to_json())

# convert the object into a dict
bank_account_entity_dict = bank_account_entity_instance.to_dict()
# create an instance of BankAccountEntity from a dict
bank_account_entity_from_dict = BankAccountEntity.from_dict(bank_account_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


