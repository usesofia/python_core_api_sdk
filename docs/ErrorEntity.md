# ErrorEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** |  | 
**messages** | **List[str]** |  | 

## Example

```python
from openapi_client.models.error_entity import ErrorEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorEntity from a JSON string
error_entity_instance = ErrorEntity.from_json(json)
# print the JSON string representation of the object
print(ErrorEntity.to_json())

# convert the object into a dict
error_entity_dict = error_entity_instance.to_dict()
# create an instance of ErrorEntity from a dict
error_entity_from_dict = ErrorEntity.from_dict(error_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


