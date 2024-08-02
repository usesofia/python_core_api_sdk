# BankTransactionEntityAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**bank_connection_id** | **str** |  | 
**bank_connection** | [**BankTransactionEntityAccountBankConnection**](BankTransactionEntityAccountBankConnection.md) |  | 
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
from python_core_api_sdk.models.bank_transaction_entity_account import BankTransactionEntityAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionEntityAccount from a JSON string
bank_transaction_entity_account_instance = BankTransactionEntityAccount.from_json(json)
# print the JSON string representation of the object
print(BankTransactionEntityAccount.to_json())

# convert the object into a dict
bank_transaction_entity_account_dict = bank_transaction_entity_account_instance.to_dict()
# create an instance of BankTransactionEntityAccount from a dict
bank_transaction_entity_account_from_dict = BankTransactionEntityAccount.from_dict(bank_transaction_entity_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


