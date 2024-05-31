# MessageTokenEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**workspace_id** | **str** |  | 
**workspace** | [**WorkspaceEntity**](WorkspaceEntity.md) |  | 
**user_id** | **str** |  | 
**user** | [**UserEntity**](UserEntity.md) |  | 
**provider** | **str** |  | 
**platform** | **str** |  | 
**device_id** | **str** |  | 
**token** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.message_token_entity import MessageTokenEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MessageTokenEntity from a JSON string
message_token_entity_instance = MessageTokenEntity.from_json(json)
# print the JSON string representation of the object
print(MessageTokenEntity.to_json())

# convert the object into a dict
message_token_entity_dict = message_token_entity_instance.to_dict()
# create an instance of MessageTokenEntity from a dict
message_token_entity_from_dict = MessageTokenEntity.from_dict(message_token_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


