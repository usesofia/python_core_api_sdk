# BalancePointResultEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_in_cents** | **float** |  | [optional] 

## Example

```python
from python_core_api_sdk.models.balance_point_result_entity import BalancePointResultEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BalancePointResultEntity from a JSON string
balance_point_result_entity_instance = BalancePointResultEntity.from_json(json)
# print the JSON string representation of the object
print(BalancePointResultEntity.to_json())

# convert the object into a dict
balance_point_result_entity_dict = balance_point_result_entity_instance.to_dict()
# create an instance of BalancePointResultEntity from a dict
balance_point_result_entity_from_dict = BalancePointResultEntity.from_dict(balance_point_result_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


