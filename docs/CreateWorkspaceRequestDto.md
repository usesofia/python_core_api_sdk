# CreateWorkspaceRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pretty_id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**business_segment** | **str** |  | [optional] 
**other_description** | **str** |  | [optional] 
**throw_after_create_workspace** | **bool** |  | [optional] 

## Example

```python
from python_core_api_sdk.models.create_workspace_request_dto import CreateWorkspaceRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkspaceRequestDto from a JSON string
create_workspace_request_dto_instance = CreateWorkspaceRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateWorkspaceRequestDto.to_json())

# convert the object into a dict
create_workspace_request_dto_dict = create_workspace_request_dto_instance.to_dict()
# create an instance of CreateWorkspaceRequestDto from a dict
create_workspace_request_dto_from_dict = CreateWorkspaceRequestDto.from_dict(create_workspace_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


