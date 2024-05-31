# MeanResultEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_in_cents** | **float** |  | 
**subcategories** | [**List[MeanResultSubcategoryItemEntity]**](MeanResultSubcategoryItemEntity.md) |  | [optional] 

## Example

```python
from python_core_api_sdk.models.mean_result_entity import MeanResultEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MeanResultEntity from a JSON string
mean_result_entity_instance = MeanResultEntity.from_json(json)
# print the JSON string representation of the object
print(MeanResultEntity.to_json())

# convert the object into a dict
mean_result_entity_dict = mean_result_entity_instance.to_dict()
# create an instance of MeanResultEntity from a dict
mean_result_entity_from_dict = MeanResultEntity.from_dict(mean_result_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


