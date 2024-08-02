# BankAccountEntityBankConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_by_user_id** | **str** |  | 
**workspace_id** | **str** |  | 
**enabled** | **bool** |  | 
**provider** | **str** |  | 
**provider_item_id** | **str** |  | 
**history_range** | **str** |  | 
**connector_id** | **str** |  | 
**connector** | [**BankConnectionEntityConnector**](BankConnectionEntityConnector.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.bank_account_entity_bank_connection import BankAccountEntityBankConnection

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountEntityBankConnection from a JSON string
bank_account_entity_bank_connection_instance = BankAccountEntityBankConnection.from_json(json)
# print the JSON string representation of the object
print(BankAccountEntityBankConnection.to_json())

# convert the object into a dict
bank_account_entity_bank_connection_dict = bank_account_entity_bank_connection_instance.to_dict()
# create an instance of BankAccountEntityBankConnection from a dict
bank_account_entity_bank_connection_from_dict = BankAccountEntityBankConnection.from_dict(bank_account_entity_bank_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


