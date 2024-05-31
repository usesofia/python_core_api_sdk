# BankConnectionWithAccountsEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_by_user_id** | **str** |  | 
**workspace_id** | **str** |  | 
**accounts** | [**List[PlainBankAccountEntity]**](PlainBankAccountEntity.md) |  | 
**enabled** | **bool** |  | 
**provider** | **str** |  | 
**provider_item_id** | **str** |  | 
**history_range** | **str** |  | 
**connector_id** | **str** |  | 
**connector** | [**BankConnectorEntity**](BankConnectorEntity.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.bank_connection_with_accounts_entity import BankConnectionWithAccountsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankConnectionWithAccountsEntity from a JSON string
bank_connection_with_accounts_entity_instance = BankConnectionWithAccountsEntity.from_json(json)
# print the JSON string representation of the object
print(BankConnectionWithAccountsEntity.to_json())

# convert the object into a dict
bank_connection_with_accounts_entity_dict = bank_connection_with_accounts_entity_instance.to_dict()
# create an instance of BankConnectionWithAccountsEntity from a dict
bank_connection_with_accounts_entity_from_dict = BankConnectionWithAccountsEntity.from_dict(bank_connection_with_accounts_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


