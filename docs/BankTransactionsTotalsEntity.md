# BankTransactionsTotalsEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries_in_cents** | **float** |  | [optional] 
**outflows_in_cents** | **float** |  | [optional] 
**outcome_in_cents** | **float** |  | [optional] 

## Example

```python
from python_core_api_sdk.models.bank_transactions_totals_entity import BankTransactionsTotalsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionsTotalsEntity from a JSON string
bank_transactions_totals_entity_instance = BankTransactionsTotalsEntity.from_json(json)
# print the JSON string representation of the object
print(BankTransactionsTotalsEntity.to_json())

# convert the object into a dict
bank_transactions_totals_entity_dict = bank_transactions_totals_entity_instance.to_dict()
# create an instance of BankTransactionsTotalsEntity from a dict
bank_transactions_totals_entity_from_dict = BankTransactionsTotalsEntity.from_dict(bank_transactions_totals_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


