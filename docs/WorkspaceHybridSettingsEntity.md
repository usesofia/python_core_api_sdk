# WorkspaceHybridSettingsEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**business_segment** | **str** |  | 
**other_business_description** | **str** |  | [optional] 

## Example

```python
from python_core_api_sdk.models.workspace_hybrid_settings_entity import WorkspaceHybridSettingsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceHybridSettingsEntity from a JSON string
workspace_hybrid_settings_entity_instance = WorkspaceHybridSettingsEntity.from_json(json)
# print the JSON string representation of the object
print(WorkspaceHybridSettingsEntity.to_json())

# convert the object into a dict
workspace_hybrid_settings_entity_dict = workspace_hybrid_settings_entity_instance.to_dict()
# create an instance of WorkspaceHybridSettingsEntity from a dict
workspace_hybrid_settings_entity_from_dict = WorkspaceHybridSettingsEntity.from_dict(workspace_hybrid_settings_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


