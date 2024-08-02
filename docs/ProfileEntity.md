# ProfileEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**full_name** | **str** |  | 
**birth_date** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.profile_entity import ProfileEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileEntity from a JSON string
profile_entity_instance = ProfileEntity.from_json(json)
# print the JSON string representation of the object
print(ProfileEntity.to_json())

# convert the object into a dict
profile_entity_dict = profile_entity_instance.to_dict()
# create an instance of ProfileEntity from a dict
profile_entity_from_dict = ProfileEntity.from_dict(profile_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


