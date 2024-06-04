# WorkspaceEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**pretty_id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**creator_user_id** | **str** |  | 
**created_at** | **datetime** |  | 
**selected_personal_category_tree_id** | **str** |  | [optional] 
**selected_business_category_tree_id** | **str** |  | [optional] 
**hybrid_settings** | [**WorkspaceHybridSettingsEntity**](WorkspaceHybridSettingsEntity.md) |  | [optional] 
**company_settings** | [**WorkspaceCompanySettingsEntity**](WorkspaceCompanySettingsEntity.md) |  | [optional] 
**personal_settings** | [**WorkspacePersonalSettingsEntity**](WorkspacePersonalSettingsEntity.md) |  | [optional] 

## Example

```python
from python_core_api_sdk.models.workspace_entity import WorkspaceEntity

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceEntity from a JSON string
workspace_entity_instance = WorkspaceEntity.from_json(json)
# print the JSON string representation of the object
print(WorkspaceEntity.to_json())

# convert the object into a dict
workspace_entity_dict = workspace_entity_instance.to_dict()
# create an instance of WorkspaceEntity from a dict
workspace_entity_from_dict = WorkspaceEntity.from_dict(workspace_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


