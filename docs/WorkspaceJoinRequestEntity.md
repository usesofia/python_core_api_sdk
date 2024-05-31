# WorkspaceJoinRequestEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**workspace_id** | **str** |  | 
**user_id** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.workspace_join_request_entity import WorkspaceJoinRequestEntity

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceJoinRequestEntity from a JSON string
workspace_join_request_entity_instance = WorkspaceJoinRequestEntity.from_json(json)
# print the JSON string representation of the object
print(WorkspaceJoinRequestEntity.to_json())

# convert the object into a dict
workspace_join_request_entity_dict = workspace_join_request_entity_instance.to_dict()
# create an instance of WorkspaceJoinRequestEntity from a dict
workspace_join_request_entity_from_dict = WorkspaceJoinRequestEntity.from_dict(workspace_join_request_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


