# MessageTokenEntityUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**password_hash** | **str** |  | [optional] 
**is_root** | **bool** |  | 
**workspaces** | [**List[UserEntityWorkspacesInner]**](UserEntityWorkspacesInner.md) |  | [optional] 
**created_at** | **object** |  | 

## Example

```python
from python_core_api_sdk.models.message_token_entity_user import MessageTokenEntityUser

# TODO update the JSON string below
json = "{}"
# create an instance of MessageTokenEntityUser from a JSON string
message_token_entity_user_instance = MessageTokenEntityUser.from_json(json)
# print the JSON string representation of the object
print(MessageTokenEntityUser.to_json())

# convert the object into a dict
message_token_entity_user_dict = message_token_entity_user_instance.to_dict()
# create an instance of MessageTokenEntityUser from a dict
message_token_entity_user_from_dict = MessageTokenEntityUser.from_dict(message_token_entity_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


