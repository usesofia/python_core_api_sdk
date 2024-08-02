# UserEntityWorkspacesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**pretty_id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**creator_user_id** | **str** |  | 
**selected_personal_category_tree_id** | **str** |  | [optional] 
**selected_business_category_tree_id** | **str** |  | [optional] 
**hybrid_settings** | [**UserEntityWorkspacesInnerHybridSettings**](UserEntityWorkspacesInnerHybridSettings.md) |  | [optional] 
**business_settings** | [**UserEntityWorkspacesInnerHybridSettings**](UserEntityWorkspacesInnerHybridSettings.md) |  | [optional] 
**personal_settings** | [**UserEntityWorkspacesInnerPersonalSettings**](UserEntityWorkspacesInnerPersonalSettings.md) |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.user_entity_workspaces_inner import UserEntityWorkspacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserEntityWorkspacesInner from a JSON string
user_entity_workspaces_inner_instance = UserEntityWorkspacesInner.from_json(json)
# print the JSON string representation of the object
print(UserEntityWorkspacesInner.to_json())

# convert the object into a dict
user_entity_workspaces_inner_dict = user_entity_workspaces_inner_instance.to_dict()
# create an instance of UserEntityWorkspacesInner from a dict
user_entity_workspaces_inner_from_dict = UserEntityWorkspacesInner.from_dict(user_entity_workspaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


