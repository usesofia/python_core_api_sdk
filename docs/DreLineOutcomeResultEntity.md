# DreLineOutcomeResultEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_in_cents** | **float** |  | 
**ratio** | **float** |  | [optional] 

## Example

```python
from python_core_api_sdk.models.dre_line_outcome_result_entity import DreLineOutcomeResultEntity

# TODO update the JSON string below
json = "{}"
# create an instance of DreLineOutcomeResultEntity from a JSON string
dre_line_outcome_result_entity_instance = DreLineOutcomeResultEntity.from_json(json)
# print the JSON string representation of the object
print(DreLineOutcomeResultEntity.to_json())

# convert the object into a dict
dre_line_outcome_result_entity_dict = dre_line_outcome_result_entity_instance.to_dict()
# create an instance of DreLineOutcomeResultEntity from a dict
dre_line_outcome_result_entity_from_dict = DreLineOutcomeResultEntity.from_dict(dre_line_outcome_result_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


