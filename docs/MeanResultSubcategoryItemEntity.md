# MeanResultSubcategoryItemEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subcategory_id** | **str** |  | 
**subcategory_name** | **str** |  | 
**amount_in_cents** | **float** |  | 

## Example

```python
from openapi_client.models.mean_result_subcategory_item_entity import MeanResultSubcategoryItemEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MeanResultSubcategoryItemEntity from a JSON string
mean_result_subcategory_item_entity_instance = MeanResultSubcategoryItemEntity.from_json(json)
# print the JSON string representation of the object
print(MeanResultSubcategoryItemEntity.to_json())

# convert the object into a dict
mean_result_subcategory_item_entity_dict = mean_result_subcategory_item_entity_instance.to_dict()
# create an instance of MeanResultSubcategoryItemEntity from a dict
mean_result_subcategory_item_entity_from_dict = MeanResultSubcategoryItemEntity.from_dict(mean_result_subcategory_item_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


