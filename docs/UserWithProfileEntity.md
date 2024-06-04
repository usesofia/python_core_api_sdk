# UserWithProfileEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**created_at** | **datetime** |  | 
**password_hash** | **str** |  | [optional] 
**profile** | [**ProfileEntity**](ProfileEntity.md) |  | 

## Example

```python
from python_core_api_sdk.models.user_with_profile_entity import UserWithProfileEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UserWithProfileEntity from a JSON string
user_with_profile_entity_instance = UserWithProfileEntity.from_json(json)
# print the JSON string representation of the object
print(UserWithProfileEntity.to_json())

# convert the object into a dict
user_with_profile_entity_dict = user_with_profile_entity_instance.to_dict()
# create an instance of UserWithProfileEntity from a dict
user_with_profile_entity_from_dict = UserWithProfileEntity.from_dict(user_with_profile_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


