# ConnectionFeatureSpecificationEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**unlimited** | **bool** |  | 
**max** | **float** |  | [optional] 
**subscription_product_id** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.connection_feature_specification_entity import ConnectionFeatureSpecificationEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionFeatureSpecificationEntity from a JSON string
connection_feature_specification_entity_instance = ConnectionFeatureSpecificationEntity.from_json(json)
# print the JSON string representation of the object
print(ConnectionFeatureSpecificationEntity.to_json())

# convert the object into a dict
connection_feature_specification_entity_dict = connection_feature_specification_entity_instance.to_dict()
# create an instance of ConnectionFeatureSpecificationEntity from a dict
connection_feature_specification_entity_from_dict = ConnectionFeatureSpecificationEntity.from_dict(connection_feature_specification_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


