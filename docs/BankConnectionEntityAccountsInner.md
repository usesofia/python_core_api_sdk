# BankConnectionEntityAccountsInner


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
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.bank_connection_entity_accounts_inner import BankConnectionEntityAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BankConnectionEntityAccountsInner from a JSON string
bank_connection_entity_accounts_inner_instance = BankConnectionEntityAccountsInner.from_json(json)
# print the JSON string representation of the object
print(BankConnectionEntityAccountsInner.to_json())

# convert the object into a dict
bank_connection_entity_accounts_inner_dict = bank_connection_entity_accounts_inner_instance.to_dict()
# create an instance of BankConnectionEntityAccountsInner from a dict
bank_connection_entity_accounts_inner_from_dict = BankConnectionEntityAccountsInner.from_dict(bank_connection_entity_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


