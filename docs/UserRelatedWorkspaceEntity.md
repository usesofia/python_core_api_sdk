# UserRelatedWorkspaceEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace** | [**UserEntityWorkspacesInner**](UserEntityWorkspacesInner.md) |  | 
**relation_type** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.user_related_workspace_entity import UserRelatedWorkspaceEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UserRelatedWorkspaceEntity from a JSON string
user_related_workspace_entity_instance = UserRelatedWorkspaceEntity.from_json(json)
# print the JSON string representation of the object
print(UserRelatedWorkspaceEntity.to_json())

# convert the object into a dict
user_related_workspace_entity_dict = user_related_workspace_entity_instance.to_dict()
# create an instance of UserRelatedWorkspaceEntity from a dict
user_related_workspace_entity_from_dict = UserRelatedWorkspaceEntity.from_dict(user_related_workspace_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


