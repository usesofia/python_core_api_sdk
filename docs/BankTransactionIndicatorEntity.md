# BankTransactionIndicatorEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**pretty_id** | **str** |  | 
**type** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**data** | **object** |  | 
**dre_line_outcome_result** | [**DreLineOutcomeResultEntity**](DreLineOutcomeResultEntity.md) |  | [optional] 
**balance_point_result** | [**BalancePointResultEntity**](BalancePointResultEntity.md) |  | [optional] 
**mean_result** | [**MeanResultEntity**](MeanResultEntity.md) |  | [optional] 
**proportion_result** | [**ProportionResultEntity**](ProportionResultEntity.md) |  | [optional] 

## Example

```python
from openapi_client.models.bank_transaction_indicator_entity import BankTransactionIndicatorEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionIndicatorEntity from a JSON string
bank_transaction_indicator_entity_instance = BankTransactionIndicatorEntity.from_json(json)
# print the JSON string representation of the object
print(BankTransactionIndicatorEntity.to_json())

# convert the object into a dict
bank_transaction_indicator_entity_dict = bank_transaction_indicator_entity_instance.to_dict()
# create an instance of BankTransactionIndicatorEntity from a dict
bank_transaction_indicator_entity_from_dict = BankTransactionIndicatorEntity.from_dict(bank_transaction_indicator_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


